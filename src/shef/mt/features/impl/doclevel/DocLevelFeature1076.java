/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package shef.mt.features.impl.doclevel;

import shef.mt.features.impl.DocLevelFeature;
import shef.mt.features.util.Sentence;
import shef.mt.features.util.Doc;

/**
 * Percentage of punctuation marks in source document
 *
 * @author Carolina Scarton
 * 
 * notice that this feature also supports extracting Chinese source language
 */
public class DocLevelFeature1076 extends DocLevelFeature {

    public DocLevelFeature1076() {
        this.setIndex(1076);
        this.setDescription("percentage of punctuation marks in source document");
    }

    public void run(Sentence source, Sentence target) {
        throw new UnsupportedOperationException("Not supported yet.");

    }

    @Override
    public void run(Doc source, Doc target) {
        int countS = 0;
        int countT = 0;
        for(int i=0;i<source.getSentences().size();i++){
            if (source.getSentence(i).isSet("count_.")) {
                countS += (Integer) source.getSentence(i).getValue("count_.");
            } else {
                countS += source.getSentence(i).countChar('.');
            }
            if (source.getSentence(i).isSet("count_,")) {
                countS += (Integer) source.getSentence(i).getValue("count_,");
            } else {
                countS += source.getSentence(i).countChar(',');
            }
            if (source.getSentence(i).isSet("count_、")) {
                countS += (Integer) source.getSentence(i).getValue("count_、");
            } else {
                countS += source.getSentence(i).countChar('、');
            }            
            if (source.getSentence(i).isSet("count_؟")) {
                countS += (Integer) source.getSentence(i).getValue("count_؟");
            } else {
                countS += source.getSentence(i).countChar('؟');
            }
            if (source.getSentence(i).isSet("count_¿")) {
                countS += (Integer) source.getSentence(i).getValue("count_¿");
            } else {
                countS += source.getSentence(i).countChar('¿');
            }
            if (source.getSentence(i).isSet("count_،")) {
                countS += (Integer) source.getSentence(i).getValue("count_،");
            } else {
                countS += source.getSentence(i).countChar('،');
            }
            if (source.getSentence(i).isSet("count_؛")) {
                countS += (Integer) source.getSentence(i).getValue("count_؛");
            } else {
                countS += source.getSentence(i).countChar('؛');
            }
            if (source.getSentence(i).isSet("count_¡")) {
                countS += (Integer) source.getSentence(i).getValue("count_¡");
            } else {
                countS += source.getSentence(i).countChar('¡');
            }
            if (source.getSentence(i).isSet("count_!")) {
                countS += (Integer) source.getSentence(i).getValue("count_!");
            } else {
                countS += source.getSentence(i).countChar('!');
            }
            if (source.getSentence(i).isSet("count_?")) {
                countS += (Integer) source.getSentence(i).getValue("count_?");
            } else {
                countS += source.getSentence(i).countChar('?');
            }
            if (source.getSentence(i).isSet("count_:")) {
                countS += (Integer) source.getSentence(i).getValue("count_:");
            } else {
                countS += source.getSentence(i).countChar(':');
            }
            if (source.getSentence(i).isSet("count_;")) {
                countS += (Integer) source.getSentence(i).getValue("count_;");
            } else {
                countS += source.getSentence(i).countChar(';');
            }
        }
        for(int i=0;i<target.getSentences().size();i++){
            if (target.getSentence(i).isSet("count_.")) {
                countT += (Integer) target.getSentence(i).getValue("count_.");
            } else {
                countT += target.getSentence(i).countChar('.');
            }
            if (target.getSentence(i).isSet("count_,")) {
                countT += (Integer) target.getSentence(i).getValue("count_,");
            } else {
                countT += target.getSentence(i).countChar(',');
            }
            if (target.getSentence(i).isSet("count_؟")) {
                countT += (Integer) target.getSentence(i).getValue("count_؟");
            } else {
                countT += target.getSentence(i).countChar('؟');
            }
            if (target.getSentence(i).isSet("count_¿")) {
                countT += (Integer) target.getSentence(i).getValue("count_¿");
            } else {
                countT += target.getSentence(i).countChar('¿');
            }
            if (target.getSentence(i).isSet("count_،")) {
                countT += (Integer) target.getSentence(i).getValue("count_،");
            } else {
                countT += target.getSentence(i).countChar('،');
            }
            if (target.getSentence(i).isSet("count_؛")) {
                countT += (Integer) target.getSentence(i).getValue("count_؛");
            } else {
                countT += target.getSentence(i).countChar('؛');
            }
            if (target.getSentence(i).isSet("count_¡")) {
                countT += (Integer) target.getSentence(i).getValue("count_¡");
            } else {
                countT += target.getSentence(i).countChar('¡');
            }
            if (target.getSentence(i).isSet("count_!")) {
                countT += (Integer) target.getSentence(i).getValue("count_!");
            } else {
                countT += target.getSentence(i).countChar('!');
            }
            if (target.getSentence(i).isSet("count_?")) {
                countT += (Integer) target.getSentence(i).getValue("count_?");
            } else {
                countT += target.getSentence(i).countChar('?');
            }
            if (target.getSentence(i).isSet("count_:")) {
                countT += (Integer) target.getSentence(i).getValue("count_:");
            } else {
                countT += target.getSentence(i).countChar(':');
            }
            if (target.getSentence(i).isSet("count_;")) {
                countT += (Integer) target.getSentence(i).getValue("count_;");
            } else {
                countT += target.getSentence(i).countChar(';');
            }
        }        
        setValue((float) Math.abs(countS - countT) / countS);
        source.setValue("noPunct", countS);
        target.setValue("noPunct", countT);
    }
}