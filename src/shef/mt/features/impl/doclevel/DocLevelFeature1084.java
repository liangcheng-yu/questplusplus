/**
 *
 */
package shef.mt.features.impl.doclevel;

import shef.mt.features.impl.DocLevelFeature;
import java.util.*;
import shef.mt.features.util.Doc;
import shef.mt.features.util.Sentence;

/**
 *
 * Percentage of content words in the source document
 *
 * @author Carolina Scarton
 *
 */
public class DocLevelFeature1084 extends DocLevelFeature {

    public DocLevelFeature1084() {
        this.setIndex(1084);
        this.setDescription("percentage of content words in the source document");
        this.addResource("source.postagger");
        
    }

    /* (non-Javadoc)
     * @see wlv.mt.features.impl.Feature#run(wlv.mt.features.util.Sentence, wlv.mt.features.util.Sentence)
     */
    @Override
    public void run(Sentence source, Sentence target) {
        // TODO Auto-generated method stub
        
    }

    @Override
    public void run(Doc source, Doc target) {
        System.out.println("=============>Inside the DocLevelFeature 1084");
        // int noContent =0;
        // int noWords =0;
        float noContent =0;
        float noWords =0;        
        for(int i=0;i<source.getSentences().size();i++){
            System.out.println("=============>Value of tokens num "+source.getSentence(i).getNoTokens());
            noWords+= source.getSentence(i).getNoTokens();
            // noContent+= (Integer) source.getSentence(i).getValue("contentWords");
            System.out.println("=============>Print the sentence text "+source.getSentence(i).getText());
            System.out.println("=============>Value of content words "+(Integer)source.getSentence(i).getValue("contentWords"));
            System.out.println("=============>Value of noun words "+(Integer)source.getSentence(i).getValue("nouns"));
            noContent += (Integer)source.getSentence(i).getValue("contentWords");
        }
        System.out.println("=============>Value of noContents"+noContent);
        System.out.println("=============>Value of noWords"+noWords);
        setValue(noContent / noWords);
    }
}
