---
UID : NE:ksmedia.KSCAMERA_EXTENDEDPROP_FOCUSSTATE
title : KSCAMERA_EXTENDEDPROP_FOCUSSTATE
author : windows-driver-content
description : This enumeration contains the focus states.
old-location : stream\kscamera_extendedprop_focusstate.htm
old-project : stream
ms.assetid : 2B74DB73-1D27-49E6-B1D8-8246FCE2F5E1
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSCAMERA_EXTENDEDPROP_FOCUSSTATE, KSCAMERA_EXTENDEDPROP_FOCUSSTATE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ksmedia.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSCAMERA_EXTENDEDPROP_FOCUSSTATE
req.alt-loc : Ksmedia.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : KSCAMERA_EXTENDEDPROP_FOCUSSTATE
---

# KSCAMERA_EXTENDEDPROP_FOCUSSTATE Enumeration
This enumeration contains the focus states.

## Syntax
````
typedef enum  { 
  KSCAMERA_EXTENDEDPROP_FOCUSSTATE_UNINITIALIZED  = 0,
  KSCAMERA_EXTENDEDPROP_FOCUSSTATE_LOST,
  KSCAMERA_EXTENDEDPROP_FOCUSSTATE_SEARCHING,
  KSCAMERA_EXTENDEDPROP_FOCUSSTATE_FOCUSED,
  KSCAMERA_EXTENDEDPROP_FOCUSSTATE_FAILED
} KSCAMERA_EXTENDEDPROP_FOCUSSTATE;
````

## Constants

<table>

<tr>
<td>KSCAMERA_EXTENDEDPROP_FOCUSSTATE_FAILED</td>
<td>The focus state is failed.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_FOCUSSTATE_FOCUSED</td>
<td>The focus state is focused.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_FOCUSSTATE_LOST</td>
<td>The focus state is lost.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_FOCUSSTATE_SEARCHING</td>
<td>The focus state is searching.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_FOCUSSTATE_UNINITIALIZED</td>
<td>The focus state is not initialized.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksmedia.h |