---
UID: NE.ks.KS_SEEKING_CAPABILITIES
title: KS_SEEKING_CAPABILITIES
author: windows-driver-content
description: .
old-location: stream\ks_seeking_capabilities.htm
old-project: stream
ms.assetid: 345ADD1F-2002-4F9C-942C-212CADCF84E5
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_SEEKING_CAPABILITIES
req.alt-loc: Ks.h
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
---

# KS_SEEKING_CAPABILITIES enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  KS_SEEKING_CanSeekAbsolute   = 0x1,
  KS_SEEKING_CanSeekForwards   = 0x2,
  KS_SEEKING_CanSeekBackwards  = 0x4,
  KS_SEEKING_CanGetCurrentPos  = 0x8,
  KS_SEEKING_CanGetStopPos     = 0x10,
  KS_SEEKING_CanGetDuration    = 0x20,
  KS_SEEKING_CanPlayBackwards  = 0x40
} KS_SEEKING_CAPABILITIES;
````


## -enum-fields
<dl>

### -field <a id="KS_SEEKING_CanSeekAbsolute"></a><a id="ks_seeking_canseekabsolute"></a><a id="KS_SEEKING_CANSEEKABSOLUTE"></a><b>KS_SEEKING_CanSeekAbsolute</b>

<dd></dd>

### -field <a id="KS_SEEKING_CanSeekForwards"></a><a id="ks_seeking_canseekforwards"></a><a id="KS_SEEKING_CANSEEKFORWARDS"></a><b>KS_SEEKING_CanSeekForwards</b>

<dd></dd>

### -field <a id="KS_SEEKING_CanSeekBackwards"></a><a id="ks_seeking_canseekbackwards"></a><a id="KS_SEEKING_CANSEEKBACKWARDS"></a><b>KS_SEEKING_CanSeekBackwards</b>

<dd></dd>

### -field <a id="KS_SEEKING_CanGetCurrentPos"></a><a id="ks_seeking_cangetcurrentpos"></a><a id="KS_SEEKING_CANGETCURRENTPOS"></a><b>KS_SEEKING_CanGetCurrentPos</b>

<dd></dd>

### -field <a id="KS_SEEKING_CanGetStopPos"></a><a id="ks_seeking_cangetstoppos"></a><a id="KS_SEEKING_CANGETSTOPPOS"></a><b>KS_SEEKING_CanGetStopPos</b>

<dd></dd>

### -field <a id="KS_SEEKING_CanGetDuration"></a><a id="ks_seeking_cangetduration"></a><a id="KS_SEEKING_CANGETDURATION"></a><b>KS_SEEKING_CanGetDuration</b>

<dd></dd>

### -field <a id="KS_SEEKING_CanPlayBackwards"></a><a id="ks_seeking_canplaybackwards"></a><a id="KS_SEEKING_CANPLAYBACKWARDS"></a><b>KS_SEEKING_CanPlayBackwards</b>

<dd></dd>
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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>