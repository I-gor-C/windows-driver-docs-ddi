---
UID: NF:ksproxy.IKsPin.KsQueryInterfaces
title: IKsPin::KsQueryInterfaces method
author: windows-driver-content
description: The KsQueryInterfaces method retrieves interfaces that a pin supports.
old-location: stream\ikspin_ksqueryinterfaces.htm
old-project: stream
ms.assetid: e8b0a1c0-c018-4556-b43c-fae4f7cf43de
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: KsQueryInterfaces method [Streaming Media Devices], KsQueryInterfaces, stream.ikspin_ksqueryinterfaces, KsQueryInterfaces method [Streaming Media Devices], IKsPin interface, ksproxy_6a22f676-b7bd-4212-a79a-3a02da890e9f.xml, IKsPin interface [Streaming Media Devices], KsQueryInterfaces method, IKsPin::KsQueryInterfaces, ksproxy/IKsPin::KsQueryInterfaces, IKsPin
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
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
req.lib: ksproxy.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	ksproxy.h
apiname:
-	IKsPin.KsQueryInterfaces
product: Windows
targetos: Windows
req.typenames: PIPE_STATE
---


# KsQueryInterfaces method
The <b>KsQueryInterfaces</b> method retrieves interfaces that a pin supports.

## Syntax

````
HRESULT KsQueryInterfaces(
  [out] PKSMULTIPLE_ITEM *InterfaceList
);
````

## Parameters

`InterfaceList`

Pointer to a buffer that receives a pointer to a <a href="..\ks\ns-ks-ksmultiple_item.md">KSMULTIPLE_ITEM</a> structure, followed by a sequence of <a href="..\ks\ns-ks-ksidentifier.md">KSPIN_INTERFACE</a> structures that describe interface types. The KSMULTIPLE_ITEM structure is a header that describes the size of the buffer and the number of entries in the list that follows the header.


## Return Value

Returns NOERROR if successful; otherwise, returns an error code.

## Remarks

The returned interfaces are ordered by preference.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | ksproxy.h (include Ksproxy.h) |
| **Library** | ksproxy.h |

## See Also

<a href="..\ks\ns-ks-ksmultiple_item.md">KSMULTIPLE_ITEM</a>

<a href="..\ks\ns-ks-ksidentifier.md">KSPIN_INTERFACE</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsPin::KsQueryInterfaces method%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>