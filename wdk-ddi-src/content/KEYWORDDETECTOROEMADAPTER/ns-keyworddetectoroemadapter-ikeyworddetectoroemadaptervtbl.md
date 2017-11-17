---
UID: NS.keyworddetectoroemadapter.IKeywordDetectorOemAdapterVtbl
title: IKeywordDetectorOemAdapterVtbl
author: windows-driver-content
description: 
ms.assetid: f5d68cb2-8217-444b-bb54-d5670d7556e8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: IKeywordDetectorOemAdapterVtbl, IKeywordDetectorOemAdapterVtbl
req.header: keyworddetectoroemadapter.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# IKeywordDetectorOemAdapterVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(IKeywordDetectorOemAdapter *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(IKeywordDetectorOemAdapter *This) AddRef			
 	
### -field ULONG(* )(IKeywordDetectorOemAdapter *This) Release			
 	
### -field HRESULT(* )(IKeywordDetectorOemAdapter *This,BOOL *SupportsUserModels,KEYWORDID **KeywordIds,ULONG *NumKeywords,LANGID **LangIds,ULONG *NumLanguages,IMFMediaType **ppMediaType) GetCapabilities			
 	
### -field HRESULT(* )(IKeywordDetectorOemAdapter *This,IStream *ModelData,KEYWORDID KeywordId,LANGID LangId,LONG KeywordEndBytePos,IMFMediaBuffer *UserRecording) VerifyUserKeyword			
 	
### -field HRESULT(* )(IKeywordDetectorOemAdapter *This,IStream *ModelData,KEYWORDSELECTOR KeywordSelector,LONG *KeywordEndBytePos,IMFMediaBuffer **UserRecordings,ULONG NumUserRecordings) ComputeAndAddUserModelData			
 	
### -field HRESULT(* )(IKeywordDetectorOemAdapter *This,IStream *UserModelData,KEYWORDSELECTOR *KeywordSelectors,ULONG NumKeywordSelectors,SOUNDDETECTOR_PATTERNHEADER **ppPatternData) BuildArmingPatternData			
 	
### -field HRESULT(* )(IKeywordDetectorOemAdapter *This,IStream *UserModelData,SOUNDDETECTOR_PATTERNHEADER *Result,KEYWORDID *KeywordId,LANGID *LangId,BOOL *pIsUserMatch,ULONG64 *KeywordStartPerformanceCounterValue,ULONG64 *KeywordEndPerformanceCounterValue) ParseDetectionResultData			
 	
## -remarks

## -see-also