---
UID: NE:keyworddetectoroemadapter.__MIDL_IKeywordDetectorOemAdapter_0002
title: "__MIDL_IKeywordDetectorOemAdapter_0002"
author: windows-driver-content
description: The KEYWORDID enumeration identifies the phrase text/function of a keyword. The value is also be used in the Windows Biometric Service adapters.
old-location: audio\keywordid.htm
old-project: audio
ms.assetid: 88D85EB1-11BC-42B9-B22E-5FB58F409C75
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: KEYWORDID, KEYWORDID enumeration [Audio Devices], KwInvalid, KwSelection, KwVoiceAssistant, __MIDL_IKeywordDetectorOemAdapter_0002, audio.keywordid, keyworddetectoroemadapter/ KwSelection, keyworddetectoroemadapter/ KwVoiceAssistant, keyworddetectoroemadapter/KEYWORDID, keyworddetectoroemadapter/KwInvalid
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: keyworddetectoroemadapter.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: KeywordDetectorOemAdapter.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	KeywordDetectorOemAdapter.h
api_name:
-	KEYWORDID
product: Windows
targetos: Windows
req.typenames: KEYWORDID
---

# __MIDL_IKeywordDetectorOemAdapter_0002 Enumeration
The <b>KEYWORDID</b> enumeration identifies the phrase text/function of a keyword. The value is also be used in the Windows Biometric Service adapters.

## Syntax
````
typedef enum  { 
  KwInvalid                 = 0,
   KwVoiceAssistant         = 1,
        KwSelection         = 2
} KEYWORDID;
````

## Constants

<table>
            
                <tr>
                    <td>KwInvalid</td>
                    <td>Indicates that the keyword was invalid.</td>
                </tr>
            
                <tr>
                    <td>KwSelection</td>
                    <td>Indicates the "select" keyword was used.</td>
                </tr>
            
                <tr>
                    <td>KwVoiceAssistant</td>
                    <td>Indicates that the "hey Cortana" keyword was used.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | keyworddetectoroemadapter.h |