---
UID: NS:ntddcdvd._AACS_CHALLENGE_KEY
title: "_AACS_CHALLENGE_KEY"
author: windows-driver-content
description: The AACS_CHALLENGE_KEY structure contains the challenge key that the device sends to the host.
old-location: storage\aacs_challenge_key.htm
old-project: storage
ms.assetid: b1eb7978-cbfc-4ffd-b345-a320e9152f03
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PAACS_CHALLENGE_KEY, AACS_CHALLENGE_KEY, AACS_CHALLENGE_KEY structure [Storage Devices], PAACS_CHALLENGE_KEY, PAACS_CHALLENGE_KEY structure pointer [Storage Devices], _AACS_CHALLENGE_KEY, ntddcdvd/AACS_CHALLENGE_KEY, ntddcdvd/PAACS_CHALLENGE_KEY, storage.aacs_challenge_key, structs-DVD_7a8e1eeb-73f5-4d10-83c6-13bac3130c91.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddcdvd.h
req.include-header: Ntddcdvd.h
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddcdvd.h
api_name:
-	AACS_CHALLENGE_KEY
product:
- Windows
targetos: Windows
req.typenames: AACS_CHALLENGE_KEY, *PAACS_CHALLENGE_KEY
---

# _AACS_CHALLENGE_KEY structure
The AACS_CHALLENGE_KEY structure contains the challenge key that the device sends to the host.

## Syntax
```
typedef struct _AACS_CHALLENGE_KEY {
  UCHAR EllipticCurvePoint[40];
  UCHAR Signature[40];
} *PAACS_CHALLENGE_KEY, AACS_CHALLENGE_KEY;
```

## Members


`EllipticCurvePoint`

The elliptical curve (ECC) point data.

`Signature`

The signature that the client uses to verify that the ECC point is valid for the current Advanced Access Content System (AACS) authentication sequence.

## Remarks
Clients retrieve the Advanced Access Content System (AACS) challenge key with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559256">IOCTL_AACS_GET_CHALLENGE_KEY</a> request. Clients send an AACS challenge key to the logical unit in an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550114">AACS_SEND_CHALLENGE_KEY</a> structure with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559302">IOCTL_AACS_SEND_CHALLENGE_KEY</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddcdvd.h (include Ntddcdvd.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550114">AACS_SEND_CHALLENGE_KEY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559256">IOCTL_AACS_GET_CHALLENGE_KEY</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559302">IOCTL_AACS_SEND_CHALLENGE_KEY</a>