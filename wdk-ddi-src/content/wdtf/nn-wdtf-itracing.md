---
UID: NN:wdtf.ITracing
title: ITracing
author: windows-driver-content
description: The ITracing interface sets an object's TTraceLevel value. This interface is a base interface for most of the WDTF interfaces.
old-location: dtf\itracing.htm
old-project: dtf
ms.assetid: 919f6ba4-ff8d-4836-b522-90c22a9221ea
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: ITracing, ITracing interface [Windows Device Testing Framework], ITracing interface [Windows Device Testing Framework], described, ITracing_b58b1d4d-7a2b-4162-ad9c-54439afd7b4a.xml, dtf.itracing, wdtf/ITracing
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtf.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: WDTF.tlb
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WDTF.tlb
api_name:
-	ITracing
-	ITracing.SetTraceLevel
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# ITracing interface

The <b>ITracing </b>interface sets an object's <a href="..\wdtf\ne-wdtf-__midl___midl_itf_wdtf_0000_0001_0001.md">TTraceLevel</a> value. This interface is a base interface for most of the WDTF interfaces.

## Methods

<p>The <b>ITracing</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ITracing::SetTraceLevel](nf-wdtf-itracing-settracelevel.md) | The SetTraceLevel method sets the tracing level for an object. |

## Remarks
Because the <a href="..\wdtf\nn-wdtf-iaction.md">IAction</a> interface inherits from the <b>ITracing</b> interface, all WDTF plug-ins will support <b>ITracing</b>. All of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff539628">WDTF core interfaces</a> should also support <b>ITracing</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wdtf.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff538787">IAction</a>



<a href="..\wdtf\ne-wdtf-__midl___midl_itf_wdtf_0000_0001_0001.md">TTraceLevel</a>



<a href="..\wdtf\nn-wdtf-itracing.md">ITracing</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [dtf\dtf]:%20ITracing interface%20 RELEASE:%20(2/23/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>