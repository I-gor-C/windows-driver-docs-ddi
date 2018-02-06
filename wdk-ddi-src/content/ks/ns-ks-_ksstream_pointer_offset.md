---
UID: NS:ks._KSSTREAM_POINTER_OFFSET
title: "_KSSTREAM_POINTER_OFFSET"
author: windows-driver-content
description: The KSSTREAM_POINTER_OFFSET structure indexes bytes or mappings within a frame.
old-location: stream\ksstream_pointer_offset.htm
old-project: stream
ms.assetid: ccbe77ee-2377-45d9-b8bf-714680c1920a
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: "_KSSTREAM_POINTER_OFFSET, avstruct_e210364b-520e-4d21-98ea-e22f5468e911.xml, *PKSSTREAM_POINTER_OFFSET, KSSTREAM_POINTER_OFFSET structure [Streaming Media Devices], KSSTREAM_POINTER_OFFSET, stream.ksstream_pointer_offset, PKSSTREAM_POINTER_OFFSET structure pointer [Streaming Media Devices], ks/KSSTREAM_POINTER_OFFSET, ks/PKSSTREAM_POINTER_OFFSET, PKSSTREAM_POINTER_OFFSET"
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
-	KSSTREAM_POINTER_OFFSET
product: Windows
targetos: Windows
req.typenames: KSSTREAM_POINTER_OFFSET, *PKSSTREAM_POINTER_OFFSET
---

# _KSSTREAM_POINTER_OFFSET structure
The KSSTREAM_POINTER_OFFSET structure indexes bytes or mappings within a frame.

## Syntax
````
typedef struct _KSSTREAM_POINTER_OFFSET {
  union {
    PUCHAR     Data;
    PKSMAPPING Mappings;
  };
  ULONG Count;
  ULONG Remaining;
} KSSTREAM_POINTER_OFFSET, *PKSSTREAM_POINTER_OFFSET;
````

## Members


## Remarks
See also <a href="https://msdn.microsoft.com/ba1c525b-26b0-4778-b58b-f4169cfb972e">AVStream DMA Services</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions. Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions. |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="..\ks\ns-ks-_ksstream_pointer.md">KSSTREAM_POINTER</a>

<a href="..\ks\ns-ks-_ksmapping.md">KSMAPPING</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSSTREAM_POINTER_OFFSET structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>