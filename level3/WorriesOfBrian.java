package kr.co.programmers;

import java.util.HashSet;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class WorriesOfBrian {
    public String solution(String sentence) {
        Set<String> charSet = new HashSet<String>();
        String regex = "([a-z])[A-Z]((?!\\1)([a-z]?)[A-Z])?(\\3[A-Z])*\\1"; // TYPE B

        Pattern p = Pattern.compile(regex);
        Matcher m = p.matcher(sentence);

        while(m.find()) {
            if (charCnt(sentence, m.group(1).charAt(0)) != 2) {
                continue;
            }

            if(charSet.contains(m.group(1))) {
                return "invalid";
            }

            charSet.add(m.group(1));
            sentence = sentence.replaceFirst(m.group(), "." + m.group().replaceAll(m.group(1), "")+ ".");
        }

        regex = "[A-Z](([a-z])[A-Z])(\\2[A-Z])*"; // TYPE A
        p = Pattern.compile(regex);
        m = p.matcher(sentence);

        while(m.find()) {
            if(charSet.contains(m.group(2))) {
                return "invalid";
            } else{
                charSet.add(m.group(2));
            }
            sentence = sentence.replaceFirst(m.group(), "." + m.group().replaceAll(m.group(2), "")+ ".");
        }

        if(sentence.matches(".*[a-z].*")) {
            return "invalid";
        }

        return sentence.replaceAll("\\.+", " ").trim();
    }

    public static long charCnt(String s, char c) {
        return s.chars().filter(ch -> ch == c).count();
    }

    public static void main(String[] args) {
        String[][] sentence = {
                {"HaEaLaLaObWORLDb",    "HELLO WORLD"},
                {"SpIpGpOpNpGJqOqA",    "SIGONG J O A"},
//                {"SpIpGpOpNpGJqOqA",    "SIGONG JOA"},
                {"AxAxAxAoBoBoB",   "invalid"},
                {"oAxAxAxAoBbB",        "AAAA BB"},
                {"HEaLLOaWORLD",        "HE LLO WORLD"},
                {"HELaLaOWORLD",        "HEL L OWORLD"},
                {"HELLaLaOaWORLD",  "HEL LLOW ORLD"},
                {"aIaAM",           "I AM"},
                {"baHELLOabWORLD",  "invalid"},
                {"aHbEbLbLbOacWdOdRdLdDc",  "HELLO WORLD"},
                {"bAaOb",   "AO"},
                {"oGOaOaGaLaEo",    "invalid"},
//                {"aHELLOa bWORLDb", "invalid"},
                {"HaEaLaLObWORLDb", "HELL O WORLD"},
                {"aHELLOWORLDa",        "HELLOWORLD"},
                {"HaEaLaLaOWaOaRaLaD",  "invalid"},
                {"abHELLObaWORLD",      "invalid"},
                {"aAbBbCa",             "ABC"},
                {"aAbBcCa",             "invalid"},
                {"abABCba",             "invalid"},
                {"Aa",                  "invalid"},
                {"aAAaAbA",             "AA AA"},
                {"aGgGaGbGbGG", "GG G G GG"},
                {"tB", "invalid"}
        };

        WorriesOfBrian wob = new WorriesOfBrian();
        for(int i = 0; i < sentence.length; i++) {
            String result = wob.solution(sentence[i][0]);
            System.out.println(result.equals(sentence[i][1]) + " " + result);
//            break;
        }
    }

}

