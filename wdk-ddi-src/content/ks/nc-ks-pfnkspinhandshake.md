---
UID: NC:ks.PFNKSPINHANDSHAKE
title: PFNKSPINHANDSHAKE
author: windows-driver-content
description: An AVStream minidriver's AVStrMiniPinHandshake routine is called when AVStream receives a protocol handshake request that it does not handle.
old-location: stream\avstrminipinhandshake.htm
old-project: stream
ms.assetid: cebeceb1-f845-42cf-9a8b-3414e4a420b6
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: AVStrMiniPinHandshake, AVStrMiniPinHandshake routine [Streaming Media Devices], PFNKSPINHANDSHAKE, avstclbk_3a87dcb0-5825-4ba0-b9b3-dfb6a1af20a2.xml, ks/AVStrMiniPinHandshake, stream.avstrminipinhandshake
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	ks.h
api_name:
-	AVStrMiniPinHandshake
product: Windows
targetos: Windows
req.typenames: SOUNDDETECTOR_PATTERNHEADER
---


# PFNKSPINHANDSHAKE callback function
An AVStream minidriver's <i>AVStrMiniPinHandshake</i> routine is called when AVStream receives a protocol handshake request that it does not handle.

## Syntax

```
PFNKSPINHANDSHAKE Pfnkspinhandshake;

NTSTATUS Pfnkspinhandshake(
  PKSPIN Pin,
  PKSHANDSHAKE In,
  PKSHANDSHAKE Out
)
{...}
```

## Parameters

`Pin`



`In`



`Out`




## Return Value

Returns STATUS_SUCCESS if the pin supports the requested protocol. Otherwise, it should return STATUS_INVALID_DEVICE_REQUEST.

## Remarks

The minidriver specifies this routine's address in the <i>Handshake</i> parameter of a call to <a href="..\ks\nf-ks-kspinregisterhandshakecallback.md">KsPinRegisterHandshakeCallback</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.  |
| **Target Platform** | Desktop |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="..\ks\nf-ks-kspinregisterhandshakecallback.md">KsPinRegisterHandshakeCallback</a>



<a href="..\ks\ns-ks-ksidentifier.md">KSIDENTIFIER</a>



<a href="..\ks\ns-ks-kshandshake.md">KSHANDSHAKE</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20PFNKSPINHANDSHAKE routine%20 RELEASE:%20(2/23/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>