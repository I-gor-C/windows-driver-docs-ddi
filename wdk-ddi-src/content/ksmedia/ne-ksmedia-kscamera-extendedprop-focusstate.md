---
UID: NE.ksmedia.KSCAMERA_EXTENDEDPROP_FOCUSSTATE
title: KSCAMERA_EXTENDEDPROP_FOCUSSTATE
author: windows-driver-content
description: This enumeration contains the focus states.
old-location: stream\kscamera_extendedprop_focusstate.htm
old-project: stream
ms.assetid: 2B74DB73-1D27-49E6-B1D8-8246FCE2F5E1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_EXTENDEDPROP_FOCUSSTATE
req.alt-loc: Ksmedia.h
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

# KSCAMERA_EXTENDEDPROP_FOCUSSTATE enumeration



## -description
<p>This enumeration contains the focus states.</p>


## -syntax

````
typedef enum  { 
  KSCAMERA_EXTENDEDPROP_FOCUSSTATE_UNINITIALIZED  = 0,
  KSCAMERA_EXTENDEDPROP_FOCUSSTATE_LOST,
  KSCAMERA_EXTENDEDPROP_FOCUSSTATE_SEARCHING,
  KSCAMERA_EXTENDEDPROP_FOCUSSTATE_FOCUSED,
  KSCAMERA_EXTENDEDPROP_FOCUSSTATE_FAILED
} KSCAMERA_EXTENDEDPROP_FOCUSSTATE;
````


## -enum-fields
<dl>

### -field KSCAMERA_EXTENDEDPROP_FOCUSSTATE_UNINITIALIZED

<dd>
<p>The focus state is not initialized.</p>
</dd>

### -field KSCAMERA_EXTENDEDPROP_FOCUSSTATE_LOST

<dd>
<p>The focus state is lost.</p>
</dd>

### -field KSCAMERA_EXTENDEDPROP_FOCUSSTATE_SEARCHING

<dd>
<p>The focus state is searching.</p>
</dd>

### -field KSCAMERA_EXTENDEDPROP_FOCUSSTATE_FOCUSED

<dd>
<p>The focus state is focused.</p>
</dd>

### -field KSCAMERA_EXTENDEDPROP_FOCUSSTATE_FAILED

<dd>
<p>The focus state is failed.</p>
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
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>