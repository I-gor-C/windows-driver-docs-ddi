---
UID: NS.wpprecorder._WPP_TRIAGE_INFO
title: WPP_TRIAGE_INFO
author: windows-driver-content
description: Used to locate the WPP log for WER reporting.
old-location: devtest\wpp_triage_info.htm
old-project: devtest
ms.assetid: BC2722A8-C09A-4C46-9EC3-45DCF4A6FD64
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: WPP_TRIAGE_INFO, WPP_TRIAGE_INFO, *PWPP_TRIAGE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wpprecorder.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WPP_TRIAGE_INFO
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
req.iface: 
req.product: Windows 10 or later.
---

# WPP_TRIAGE_INFO structure



## -description
<p>Used to locate the WPP log
for WER reporting.</p>


## -syntax

````
typedef struct _WPP_TRIAGE_INFO {
  ULONG WppAutoLogHeaderSize;
  ULONG WppDriverContextOffset;
  ULONG WppAutoLogHeaderSizeOffset;
  ULONG WppSizeOfAutoLogHeaderSizeField;
  ULONG WppDriverContextSize;
} WPP_TRIAGE_INFO, *PWPP_TRIAGE_INFO;
````


## -struct-fields
<dl>

### -field WppAutoLogHeaderSize

<dd>
<p>Size of WPP_AUTOLOG_HEADER.</p>
</dd>

### -field WppDriverContextOffset

<dd>
<p>Offset of DriverContext into WPP_AUTOLOG_HEADER.</p>
</dd>

### -field WppAutoLogHeaderSizeOffset

<dd>
<p>Offset of Size field into WPP_AUTOLOG_HEADER.</p>
</dd>

### -field WppSizeOfAutoLogHeaderSizeField

<dd>
<p> Size of Header size field.</p>
</dd>

### -field WppDriverContextSize

<dd>
<p> Size of WPP_AUTOLOG_CONTEXT.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wpprecorder.h</dt>
</dl>
</td>
</tr>
</table>