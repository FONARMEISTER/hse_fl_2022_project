- Арифметика:
Выделяется наличием левой рекурсии. По неизвестной причине огромные деревья вывода при обработке получают Segmentation Fault. Вероятно, питон на моей машине не справляется с такой большой рекурсией(recursionlimit был увеличен) и неоптимальной грамматикой. Поэтому на больших тестах у меня есть только время построения дерева. На тестах поменьше есть ещё время обхода.
  - basic
    - Parse Tree building time : 0.011461257934570312 seconds
    - Evaluating time: 0.0011436939239501953 seconds

  - no-paren(50000 символов)
    - Parse Tree building time : 1.0959234237670898 seconds
    - Evaluating time: 0.07884860038757324 seconds

  - ones(25000 символов)
    - Parse Tree building time : 0.6678214073181152 seconds
    - Evaluating time: 0.035704612731933594 seconds

  - paren(100000 символов)
    - Parse Tree building time : 2.3594186305999756 seconds
    - Evaluating time: 0.14466309547424316 seconds

  - no-parenLarge(1000000 символов)
    - Parse Tree building time : 23.172285318374634 seconds

  - onesLarge(1000000 символов)
    - Parse Tree building time : 25.919100046157837 seconds

  - parenLarge(1000000 символов)
    - Parse Tree building time : 24.824243783950806 seconds

- Арифметика2:
Также левая рекурсия. Так как здесь хорошая арифметика, на миллионе элементов нету SegFault, а также дерево строится побыстрее. Ура!
  - basic
    - Parse Tree building time : 0.0061566829681396484 seconds
    - Evaluating time: 0.0008540153503417969 seconds

  - no-paren(50000 символов)
    - Parse Tree building time : 0.9025664329528809 seconds
    - Evaluating time: 0.03661155700683594 seconds

  - ones(25000 символов)
    - Parse Tree building time : 0.5455241203308105 seconds
    - Evaluating time: 0.023325443267822266 seconds

  - paren(100000 символов)
    - Parse Tree building time : 2.2548165321350098 seconds
    - Evaluating time: 0.07297301292419434 seconds

  - no-parenLarge(1000000 символов)
    - Parse Tree building time : 18.460972547531128 second
    - Evaluating time: 0.6825952529907227 seconds

  - onesLarge(1000000 символов)
    - Parse Tree building time : 22.653791427612305 seconds
    - Evaluating time: 0.83414626121521 seconds

  - parenLarge(1000000 символов)
    - Parse Tree building time : 20.86322855949402 seconds
    - Evaluating time: 0.6323146820068359 seconds

- ПСП.
Выделяется отсутствием любых лево-рекурсивных проблем. Аналогично с первой арифметикой на больших тестах только построение дерева.
  - basic
    - Parse Tree building time : 0.009206533432006836 seconds
    - Walking time: 0.0005977153778076172 seconds

  - just-psp(20000 символов)
    - Parse Tree building time : 0.659609317779541 seconds
    - Walking time: 0.04342508316040039 seconds

  - multiple-psp(20000 символов)
    - Parse Tree building time : 0.5700304508209229 seconds
    - Walking time: 0.07888436317443848 seconds

  - open-close(20000 символов)
    - Parse Tree building time : 0.5783898830413818 seconds
    - Walking time: 0.07145285606384277 seconds

  - open-then-close(20000 символов)
    - Parse Tree building time : 0.6221344470977783 seconds
    - Walking time: 0.10057449340820312 seconds

  - just-pspLarge(150000 символов, на бОльшем количестве(200000) SegFault)
    - Parse Tree building time : 5.142838954925537 seconds

  - multiple-pspLarge(1000000 символов)
    - Parse Tree building time : 33.6783766746521 seconds

  - open-closeLarge(40000 символов, на бОльших SegFault вероятно из-за специфики грамматики Дика для ПСП)
    - Parse Tree building time : 1.5233230590820312 seconds

  - open-then-closeLarge(40000 символов, по тем же причинам)
    - Parse Tree building time : 1.1857211589813232 seconds
  