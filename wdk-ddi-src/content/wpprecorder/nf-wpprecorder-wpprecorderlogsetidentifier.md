---
UID: NF.wpprecorder.WppRecorderLogSetIdentifier
title: WppRecorderLogSetIdentifier macro
author: windows-driver-content
description: The WppRecorderLogSetIdentifier method sets a string identifier for the recorder log.
old-location: devtest\wpprecorderlogsetidentifier.htm
old-project: devtest
ms.assetid: E2687B3C-2BCF-4764-99E0-4495296F14C4
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: WppRecorderLogSetIdentifier
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wpprecorder.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WppRecorderLogSetIdentifier
req.alt-loc: Wpprecorder.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# WppRecorderLogSetIdentifier macro



## -description
The <a href="devtest.wpprecorderlogsetidentifier">WppRecorderLogSetIdentifier</a> method sets a string identifier for the recorder log.



## -syntax

````
NTSTATUS WppRecorderLogSetIdentifier(
   NULL RecorderLog,
   NULL LogIdentifier
);
````


## -parameters

### -param RecorderLog 

A recorder log handle returned in a previous call to WppRecorderLogCreate.


### -param LogIdentifier 

A string identifier to set.


## -remarks
Do not call <a href="devtest.wpprecorderlogsetidentifier">WppRecorderLogSetIdentifier</a> on the default log handle returned by <a href="devtest.wpprecorderloggetdefault">WppRecorderLogGetDefault</a>.


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wpprecorder.h</dt>
</dl>
</td>
</tr>
</table>