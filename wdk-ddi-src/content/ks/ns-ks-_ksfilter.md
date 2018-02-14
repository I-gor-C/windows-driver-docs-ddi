---
UID: NS:ks._KSFILTER
title: "_KSFILTER"
author: windows-driver-content
description: The KSFILTER structure describes an instantiated filter.
old-location: stream\ksfilter.htm
old-project: stream
ms.assetid: b9233f69-1ddf-4133-afd3-150aef5fc4a0
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: PKSFILTER structure pointer [Streaming Media Devices], ks/PKSFILTER, KSFILTER structure [Streaming Media Devices], KSFILTER, _KSFILTER, stream.ksfilter, PKSFILTER, avstruct_6662a03a-c6de-4f5e-b86a-a3685dba320e.xml, *PKSFILTER, ks/KSFILTER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
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
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ks.h
apiname:
-	KSFILTER
product: Windows
targetos: Windows
req.typenames: "*PKSFILTER, KSFILTER"
---

# _KSFILTER structure
The KSFILTER structure describes an instantiated filter.

## Syntax
````
typedef struct _KSFILTER {
  const KSFILTER_DESCRIPTOR *Descriptor;
  KSOBJECT_BAG              Bag;
  PVOID                     Context;
} KSFILTER, *PKSFILTER;
````

## Members


## Remarks
Drivers implementing software filters typically associate filter state with the KSFILTER structure. Software filters usually process data within the callback specified by the <b>Process</b> member of the corresponding <a href="..\ks\ns-ks-_ksfilter_dispatch.md">KSFILTER_DISPATCH</a> structure.

Hardware filters typically do not use KSFILTER because the focus of the hardware driver is the platform transition: the movement of data between the host and the external hardware. This transition is typically handled by code associated with an AVStream queue object.

Also see <a href="https://msdn.microsoft.com/b7ee5756-1c79-4ead-9999-d13be9a0d3d9">Object Bags</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions. Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions. |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="..\ks\ns-ks-_ksfilter_descriptor.md">KSFILTER_DESCRIPTOR</a>



<a href="..\ks\nf-ks-kscompletependingrequest.md">KsCompletePendingRequest</a>



<a href="..\ks\ns-ks-_ksfilter_dispatch.md">KSFILTER_DISPATCH</a>



<a href="..\ks\nf-ks-ksadditemtoobjectbag.md">KsAddItemToObjectBag</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSFILTER structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>