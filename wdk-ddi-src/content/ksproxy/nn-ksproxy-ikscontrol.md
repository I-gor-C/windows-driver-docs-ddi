---
UID: NN:ksproxy.IKsControl
title: IKsControl
author: windows-driver-content
description: The IKsControl interface provides user-mode methods that control a KS filter or KS pin. See the IKsControl AVStream COM interface for information about the user-mode equivalent of this interface.
old-location: stream\ikscontrol.htm
old-project: stream
ms.assetid: d73cf2fc-15bb-4f45-aae3-fb55bcd072a3
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: stream.ikscontrol, IKsControl interface [Streaming Media Devices], IKsControl interface [Streaming Media Devices], described, IKsControl, ksproxy/IKsControl, ksproxy_59a4df2f-d723-499a-adc6-907c0592a6ac.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: ksproxy.h
req.include-header: Ksproxy.h
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
req.type-library: 
req.lib: Ksproxy.lib
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	Ksproxy.lib
-	Ksproxy.dll
apiname:
-	IKsControl
product: Windows
targetos: Windows
req.typenames: PIPE_STATE
---

# IKsControl interface

The <b>IKsControl</b> interface provides user-mode methods that control a KS filter or KS pin. See the <a href="..\ksproxy\nn-ksproxy-ikscontrol.md">IKsControl</a> AVStream COM interface for information about the user-mode equivalent of this interface.

## Methods

<p>The <b>IKsControl</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ksproxy.IKsControl.KsEvent](nf-ksproxy-ikscontrol-ksevent.md) | The KsEvent method enables or disables an event, along with any other defined support operations available on an event set. |
| [ksproxy.IKsControl.KsMethod](nf-ksproxy-ikscontrol-ksmethod.md) | The KsMethod method sends a method to a KS object, along with any other defined support operations available on a method set. |
| [ksproxy.IKsControl.KsProperty](nf-ksproxy-ikscontrol-ksproperty.md) | The KsProperty method sets a property or retrieves property information, along with any other defined support operations available on a property set. |

## Remarks

The IID for this interface is IID_IKsControl.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ksproxy.h (include Ksproxy.h) |

## See Also

<a href="..\ksproxy\nn-ksproxy-ikscontrol.md">IKsControl (AVStream COM Interface)</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsControl interface%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>