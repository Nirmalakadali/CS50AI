import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    num_pages = len(corpus)
    if page not in corpus or not corpus[page]:
        return {p: 1 / num_pages for p in corpus}
    linked_pages_prob = {p: damping_factor / len(corpus[page]) for p in corpus[page]}
    all_pages_prob = (1 - damping_factor) / num_pages
    probability_distribution_dict = {
        p: linked_pages_prob.get(p, 0) + all_pages_prob for p in corpus
    }

    return probability_distribution_dict


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    estimated_pagerank={page: 0 for page in corpus}
    first_sample_page=random.choice(list(corpus.keys()))
    for _ in range(n):
        probability=transition_model(corpus,first_sample_page,damping_factor)
        next_page=random.choices(list(probability.keys()),weights=list(probability.values()))[0]
        estimated_pagerank[next_page]+=1
        first_sample_page=next_page
    total_samples=sum(estimated_pagerank.values())
    estimated_pagerank={page:count/total_samples for page ,count in estimated_pagerank.items()}

    return estimated_pagerank




def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N=len(corpus)
    estimated_pagerank={page:1/N for page in corpus}

    while True:
        new_pagerank={}

        for page in corpus:
            new_pagerank[page]=(1-damping_factor)/N

            for incoming,links in corpus.items():
                if page in links:
                    if(len(links)==0):
                        num_links=N
                    else:
                        num_links=len(links)
                    new_pagerank[page]+=damping_factor*(estimated_pagerank[incoming]/num_links)

        if all(abs(new_pagerank[page]-estimated_pagerank[page])<0.001 for page in corpus):
            break
        estimated_pagerank=new_pagerank
    return estimated_pagerank


if __name__ == "__main__":
    main()


