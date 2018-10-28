# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 13:54:51 2018

@author: IstukiHamano
"""
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import (Features,CategoriesOptions,ConceptsOptions,
                                                                      EmotionOptions,EntitiesOptions,
                                                                      KeywordsOptions,MetadataOptions,
                                                                      RelationsOptions,SemanticRolesOptions,
                                                                      SentimentOptions)

natural_language_understanding=NaturalLanguageUnderstandingV1(
        version='2018-10-28',
        username='各自で入れてください',
        password='各自で入れてください',
        url='各自で入れてください'
        )
"""
#GET要求で、テキストを解析する場合
response=natural_language_understanding.analyze(
        text='my name is Hamano''I fine thank you''長濱ねるがこの世で一番可愛い',
        features=Features(
                entities=EntitiesOptions(#概念の解析する
                        emotion=True,
                        sentiment=True,
                        limit=2),
                keywords=KeywordsOptions(#コンテンツ内の重要語を解析する
                        emotion=True,
                        sentiment=True,
                        limit=5))).get_result()  
print(json.dumps(response,indent=2))
"""

#POST要求で、URLから解析する場合
response=natural_language_understanding.analyze(
        url='http://edmmaxx.com/news/19671',
        features=Features(
                concepts=ConceptsOptions(#テキストに関連するカテゴリを解析
                        limit=3),
                categories=CategoriesOptions(),#上位3カテゴリを解析
                emotion=EmotionOptions(#テキスト本文全体、またはtargeのフレーズに対する感情を解析（前後のフレーズより解析する）＊日本語対応してない
                        targets=['音楽','EDM','仕事','人生']),
                entities=EntitiesOptions(#概念の解析
                        sentiment=True,
                        limit=1),
                keywords=KeywordsOptions(#コンテンツ内のキーワードを解析
                        sentiment=True,
                        emotion=True,#検出されたキーワードの感情を解析
                        limit=10),#返すキーワードの数、デフォルト50、最大250
                metadata=MetadataOptions(),#WEBとHTML限定、ページのメタデータ（著者名、タイトル、公開日など）解析
                relations=RelationsOptions(),#単語同士の相関を解析
                #semantic_roles=SemanticRolesOptions()#テキストを主語、述語、目的語の形式に解析
                sentiment=SentimentOptions(#テキストやターゲットの一般的な感情を分析（学習させた文章でなく一般的な使い方から感情解析
                        targets=['音楽','EDM','仕事','人生']))).get_result()
print(json.dumps(response,indent=2))
