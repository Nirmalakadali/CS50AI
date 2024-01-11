# Analysis

## Layer 3, Head 1

Sentence-1: She whispered a secret to the [MASK].

Output Sentences :

1) She whispered a secret to the others.
2) She whispered a secret to the crowd.
3) She whispered a secret to the sky.

Explanation:
In this case, this attention head appears to have learned a very clear pattern: each word is paying attention to the word that immediately follows it. The word "she", for example, is represented by the second row of the diagram, and in that row the brightest cell is the cell corresponding to the "whisphered" column, suggesting that the word "she" is attending strongly to the word "whisphered". The same holds true for the other tokens in the sentence.

Sentence-2: I placed the [MASK] carefully on the shelf.

Output Sentences:

1) I placed the book carefully on the shelf.
2) I placed the box carefully on the shelf.
3) I placed the books carefully on the shelf.
Explanation:
In this case, this attention head appears to have learned a very clear pattern: each word is paying attention to the word that immediately follows it. The word "I", for example, is represented by the second row of the diagram, and in that row the brightest cell is the cell corresponding to the "placed" column, suggesting that the word "I" is attending strongly to the word "placed". The same holds true for the other tokens in the sentence.

## Layer 2, Head 7

Sentence-1: Sentence 1: "The cat chased the [MASK] through the garden."

Output Sentences:

1) The cat chased the cat through the garden
2) The cat chased the dog through the garden
3) The cat chased the mouse through the garden

Explanation:
In this case, The attention head appears to focus on the direct object of the verb "chased." In this context, the direct object is the word that represents the entity being pursued or chased by the cat. The attention head pays strong attention to the word that follows the verb "chased," indicating that it recognizes and emphasizes the relationship between the verb and its direct object.

Sentence-2 : The [MASK] circled overhead, scanning the terrain.

Output Sentences:

1) The helicopter circled overhead, scanning the terrain.
2) The plane circled overhead, scanning the terrain.
3) The helicopters circled overhead, scanning the terrain.

Explanation:
In this case,the attention head might be emphasizing the relationship between the subject and the action. The subject is the entity performing the action of circling overhead, and the attention head appears to focus on the adverb "overhead" and its connection with the subject. In other words, it is paying attention to the word that represents the entity carrying out the action, highlighting the relationship between the subject and the specific action.
