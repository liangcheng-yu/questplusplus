/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package shef.mt.features.impl.doclevel;

import java.util.HashSet;
import shef.mt.features.impl.DocLevelFeature;
import shef.mt.features.util.Doc;
import shef.mt.features.util.Sentence;
import java.util.*;


/**
 * Number of occurrences of the target word within the target hypothesis (averaged for all words in the hypothesis - type/token ratio)
 * 
 * @author Carolina Scarton
 */
public class DocLevelFeature1021 extends DocLevelFeature{
    
    public DocLevelFeature1021() {
        this.setIndex(1021);
        this.setDescription("");
    }

    @Override
    public void run(Sentence source, Sentence target) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public void run(Doc source, Doc target) {
        // Create a hashtable to store the token occurence mapping
        Hashtable<String, Integer> occurenceCountTable
        = new Hashtable<String, Integer>();
        int numTotalTokens=0;
        int prevCtr;

        // Log the occurences
        for(int i=0; i<source.getSentences().size(); i++){
            numTotalTokens+= source.getSentence(i).getNoTokens();
            String[] tokens = source.getSentence(i).getTokens();
            for (String token : tokens) {
                if (occurenceCountTable.contains(token.toLowerCase())){
                    prevCtr = occurenceCountTable.get(token.toLowerCase());
                    occurenceCountTable.put(token.toLowerCase(), prevCtr+1);
                }
                else{
                    occurenceCountTable.put(token.toLowerCase(), 1);
                }
            }
        } 
        // Find the number of tokens that appear 1 time only
        int numTokensAppearOnce = 0;
        Enumeration allKeys = occurenceCountTable.keys();
        while (allKeys.hasMoreElements()) { 
            if(occurenceCountTable.get(allKeys.nextElement())==1){
                numTokensAppearOnce += 1;
            } 
        }        

        setValue((float) numTokensAppearOnce / numTotalTokens); 
        
    }
}
