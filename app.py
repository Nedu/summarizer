from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

def create_frequency_table(text_string) -> dict:
    #removing stop words
    stop_words = set(stopwords.words("english"))
    
    words = word_tokenize(text_string)
    
    #reducing words to their root form
    ps = PorterStemmer()
    
    #creating dictionary for the word frequency table
    frequency_table = dict()
    for word in words:
        word = ps.stem(word)
        if word in stop_words:
            continue
        if word in frequency_table:
            frequency_table[word] += 1
        else:
            frequency_table[word] = 1

    return frequency_table

def score_sentences(sentences, freqTable) -> dict:
    """
    score a sentence by its words
    Basic algorithm: adding the frequency of every non-stop word in a sentence divided by total no of words in a sentence.
    :rtype: dict
    """

    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        word_count_in_sentence_except_stop_words = 0
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                word_count_in_sentence_except_stop_words += 1
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        if sentence[:10] in sentenceValue:
            sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] / word_count_in_sentence_except_stop_words

        '''
        Notice that a potential issue with our score algorithm is that long sentences will have an advantage over short sentences. 
        To solve this, we're dividing every sentence score by the number of words in the sentence.
        
        Note that here sentence[:10] is the first 10 character of any sentence, this is to save memory while saving keys of
        the dictionary.
        '''

    return sentenceValue

def find_average_score(sentenceValue) -> int:
    """
    Find the average score from the sentence value dictionary
    :rtype: int
    """
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original text
    average = (sumValues / len(sentenceValue))

    return average

def generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] >= (threshold):
            summary += " " + sentence
            sentence_count += 1

    return summary

def get_summary(story):
    # Create the word frequency table
    freq_table = create_frequency_table(story)

    '''
    We already have a sentence tokenizer, so we just need 
    to run the sent_tokenize() method to create the array of sentences.
    '''

    # Tokenize the sentences
    sentences = sent_tokenize(story)

    # Important Algorithm: score the sentences
    sentence_scores = score_sentences(sentences, freq_table)

    # Find the threshold
    threshold = find_average_score(sentence_scores)

    # Important Algorithm: Generate the summary
    summary = generate_summary(sentences, sentence_scores, 1.8 * threshold)

    return summary

if __name__ == '__main__':
    story = '''Dae was the sun and Knight was a curious man.
Knight noticed Dae shining as brilliantly as diamonds on fire in the sky.  He was in awe of her warm glow and adored her from Earth.  She was so bright that it hurt his eyes to look upon her directly.  Dae loved Knight as well, she noticed the effort he made to admire her and wished for him to be close to her.  He could never look at her nor reach for her without being in great pain!  She was so bright!  It made Dae sorrowful to know her glow was painful to her Knight.  Yet, she was the sun, she provided Earth with warmth and light.  It was in her nature to shine and there was no other way for her to be less sun.  Their love was tragic yet true.  They both wished for the same thing, to hold each other and love together for eternity but they could not as it caused them both great discomfort.
Knight was very clever.  He decided to craft armour made of his devotion to Dae to shield himself from her mighty fire.  He thought, “That I may safely reach out to Dae without being burned to ash nor blinded by her wonderful touch.  ” Surely, this material would withstand her powerful being and they could be together finally.  Dae watched Knight toil diligently over the armour.
At long last, he came to Dae after his beautiful, gleaming armor was crafted.  She eagerly reached out to him but she melted his armor in just a moment!   “Oh no!”, she exclaimed.  She hadn’t meant to do this!  Knight was taken aback and disappointed that his armour was so easily destroyed, but he still adored her.  However, Dae was also upset that her touch had caused him so much grief.  Their love was tragic yet true.  They both wished for the same thing, to hold and love each other for all time.  But, they could not be together as it caused them both discomfort.
No matter to Knight, he used his enormous heart to fashion himself a cloak made of his love for Dae.  It was the strongest material ever made in all of time!  Surely, this time, the cloak would withstand her mighty touch and they could finally be together.
Knight then covered himself with the cloak and went to Dae once more.  He was a man in love, determined to hold Dae close to him.  When she saw him in the cloak she was overcome with joy and shone brighter than ever.  This made Knight nervous, the cloak was very delicate.  He was unsure if it would be destroyed by her intense rays.  He reached out to her anyway.  Then, something magical happened!  They were able to finally hold each other!  Knight gave her happiness and she wished to return that joy to him.  The cloak allowed them to be close!  She asked him if he would like to become a Moon.  He joyfully accepted!
For some time, they stayed close to each other, though his light was pale in comparison to her wondrous glow.  When he became the moon, the beings of Earth were in awe of him.  Knight was very kind and he loved Dae very much, so would never ask her to shine less than him.  He asked her if she would like to try on his cloak instead.  Dae was delighted that he would offer his lovely cloak to be wrapped around her celestial body, she agreed.  When Dae put on the cloak, something amazing happened!  The space around her was immediately draped with darkness.  Neither of them expected that!  But, the beings of Earth fell in love with Knight!  And they began to sing and praise him as they had praised Dae.  When Dae saw this, she loved Knight even more, if it were possible!  They remained this way for some time.
However, the Earth was getting sick without Daes warmth and light.  She made Knight aware of this and he became sad, because he knew his pale light was not enough in comparison to the gift her brilliance gave the Earth.  Knight was very intelligent.  He knew that without the Earth, he would recieve no praise from the beings who lived there.  He had compassion for them as he was once a mortal human himself.
So Knight and Dae made a promise together.  Dae would wear Knight’s cloak for a short time so that they both could shine in their own way for those who loved them most.  Dae and Knight love each other so much, they take turns wearing Knight’s cloak made of his pure love for her.  Dae shines always and Knight is always close to her proving his devotion and love.  Just as they had wanted all along.  No more did they suffer.  Their love is true but no longer tragic.'''
    summary = get_summary(story)
    print(summary)