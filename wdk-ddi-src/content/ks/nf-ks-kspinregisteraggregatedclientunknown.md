---
UID : NF:ks.KsPinRegisterAggregatedClientUnknown
title : KsPinRegisterAggregatedClientUnknown function
author : windows-driver-content
description : This inline function is a wrapper for KsRegisterAggregatedClientUnknown.
old-location : stream\kspinregisteraggregatedclientunknown.htm
old-project : stream
ms.assetid : 302d87be-a276-49ea-98f2-89e1f231c3c6
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KsPinRegisterAggregatedClientUnknown
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ks.h
req.include-header : Ks.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KsPinRegisterAggregatedClientUnknown
req.alt-loc : ks.h
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
req.typenames : 
---


# KsPinRegisterAggregatedClientUnknown function
This inline function is a wrapper for <a href="..\ks\nf-ks-ksregisteraggregatedclientunknown.md">KsRegisterAggregatedClientUnknown</a>.

## Syntax

````
PUNKNOWN __inline KsPinRegisterAggregatedClientUnknown(
  _In_ PKSPIN   Pin,
  _In_ PUNKNOWN ClientUnknown
);
````

## Parameters

`Pin`

A pointer to a <a href="..\ks\ns-ks-_kspin.md">KSPIN</a> structure.

`ClientUnknown`

A pointer to an <b>IUnknown</b> interface.


## Return Value

<b>KsPinRegisterAggregatedClientUnknown</b> returns the newly created aggregate object.

## Remarks

This inline function only performs a typecast and then calls <a href="..\ks\nf-ks-ksregisteraggregatedclientunknown.md">KsRegisterAggregatedClientUnknown</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\ks\nf-ks-ksregisteraggregatedclientunknown.md">KsRegisterAggregatedClientUnknown</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinRegisterAggregatedClientUnknown function%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>