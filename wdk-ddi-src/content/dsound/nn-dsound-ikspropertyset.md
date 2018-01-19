---
UID : NN:dsound.IKsPropertySet
title : IKsPropertySet
author : windows-driver-content
description : The IKsPropertySet interface provides methods that access properties of KS objects that are implemented in a KS minidriver.
old-location : stream\ikspropertyset.htm
old-project : stream
ms.assetid : 9999d6ec-977c-4425-ad38-0c5478272c76
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : IKsPropertySet, IKsPropertySet::Set, Set
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : dsound.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IKsPropertySet
req.alt-loc : dsound.h
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
req.typenames : DRMRIGHTS, *PDRMRIGHTS
---

# IKsPropertySet interface

The <b>IKsPropertySet</b> interface provides methods that access properties of KS objects that are implemented in a KS minidriver.

The IID for this interface is IID_IKsPropertySet.

## Methods

<p>The <b>IKsPropertySet</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dsound.IKsPropertySet.Set](nf-dsound-ikspropertyset-set.md) | The Set method sets a property identified by a property-set GUID and a property identifier. |

## Remarks

The <b>IKsPropertySet</b> interface methods translate user-mode property requests into kernel-mode property sets that are used by KS minidrivers. 

KS objects include, for example, KS filters, KS pins, and KS clocks. </p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | dsound.h |
| **DLL** |  |