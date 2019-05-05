package shef.mt.features.impl.doclevel;


import shef.mt.features.impl.DocLevelFeature;
import shef.mt.features.util.Doc;
import shef.mt.features.util.Sentence;

import java.util.*;


/**
 * Average token length in target (document-level)
 *
 */
public class DocLevelFeature1007 extends DocLevelFeature {

    public DocLevelFeature1007() {
        this.setIndex(1007);
        this.setDescription("average target token length");
    }

    @Override
    public void run(Doc source, Doc target) {
        
        double avg_doc = 0.0;
        ArrayList<Sentence> sentences = target.getSentences();
        for (int i=0; i<sentences.size();i++){
            double avg_sent=0.0;
            String[] tokens = sentences.get(i).getTokens();
            int noChars = 0;
            int noTokens = tokens.length;
            for (String token : tokens) {
                noChars += token.length();
            }
            avg_sent = (float) noChars / noTokens;
            avg_doc+=avg_sent;
        }
        setValue((float) avg_doc/sentences.size());
    }

    @Override
    public void run(Sentence source, Sentence target) {
        throw new UnsupportedOperationException("Not supported yet.");
    }
    
}
