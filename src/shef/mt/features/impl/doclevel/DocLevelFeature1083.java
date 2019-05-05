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
 * Percentage of content words in the target document
 *
 * @author Carolina Scarton
 *
 */
public class DocLevelFeature1083 extends DocLevelFeature {

    public DocLevelFeature1083() {
        this.setIndex(1083);
        this.setDescription("percentage of content words in the target document");
        this.addResource("target.postagger");
        
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
        System.out.println("=============>Inside the DocLevelFeature 1083");
        float noContent =0;
        float noWords =0;
        for(int i=0;i<target.getSentences().size();i++){
            System.out.println("=============>Value of tokens num "+target.getSentence(i).getNoTokens());
            noWords+= target.getSentence(i).getNoTokens();
            System.out.println("=============>Value of content words "+(Integer)target.getSentence(i).getValue("contentWords"));
            System.out.println("=============>Value of noun words "+(Integer)target.getSentence(i).getValue("nouns"));
            noContent+= (Integer) target.getSentence(i).getValue("contentWords");
        }
        System.out.println("=============>Value of noContents"+noContent);
        System.out.println("=============>Value of noWords"+noWords);
        setValue(noContent / noWords);
    }
}
