---
UID: NS:ks._KSDEVICE_DESCRIPTOR
title: "_KSDEVICE_DESCRIPTOR"
author: windows-driver-content
description: The KSDEVICE_DESCRIPTOR structure describes the characteristics of a particular device.
old-location: stream\ksdevice_descriptor.htm
old-project: stream
ms.assetid: dc68f6d8-a2d5-4940-a708-fe761c3a8a0d
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: ks/PKSDEVICE_DESCRIPTOR, PKSDEVICE_DESCRIPTOR, PKSDEVICE_DESCRIPTOR structure pointer [Streaming Media Devices], *PKSDEVICE_DESCRIPTOR, stream.ksdevice_descriptor, KSDEVICE_DESCRIPTOR, _KSDEVICE_DESCRIPTOR, KSDEVICE_DESCRIPTOR structure [Streaming Media Devices], avstruct_b51d9c2c-278f-4357-b84a-da6959ea9959.xml, ks/KSDEVICE_DESCRIPTOR
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
-	KSDEVICE_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: KSDEVICE_DESCRIPTOR, *PKSDEVICE_DESCRIPTOR
---

# _KSDEVICE_DESCRIPTOR structure
The KSDEVICE_DESCRIPTOR structure describes the characteristics of a particular device.

## Syntax
````
typedef struct _KSDEVICE_DESCRIPTOR {
  const KSDEVICE_DISPATCH   *Dispatch;
  ULONG                     FilterDescriptorsCount;
  const KSFILTER_DESCRIPTOR *FilterDescriptors;
  ULONG                     Version;
  ULONG                     Flags;
} KSDEVICE_DESCRIPTOR, *PKSDEVICE_DESCRIPTOR;
````

## Members


## Remarks
Most often, this structure is used in conjunction with <a href="..\ks\nf-ks-ksinitializedriver.md">KsInitializeDriver</a> in the client's <b>DriverEntry</b> function to initialize the device. This structure is also used to manually initialize or create devices with the <a href="..\ks\nf-ks-ksinitializedevice.md">KsInitializeDevice</a> and <a href="..\ks\nf-ks-kscreatedevice.md">KsCreateDevice</a> functions.

If you set <b>Version</b> to KSDEVICE_DESCRIPTOR_VERSION_2 and run your driver on an early version of AVStream that does not support <b>Flags</b>, all flags will be considered to be zero.

Similarly, using an earlier version descriptor on later versions of AVStream causes no flags to be specified.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions. Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions. |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="..\ks\nf-ks-kscreatedevice.md">KsCreateDevice</a>



<a href="..\ks\nf-ks-ksinitializedevice.md">KsInitializeDevice</a>



<a href="..\ks\ns-ks-_ksfilter_descriptor.md">KSFILTER_DESCRIPTOR</a>



<a href="..\ks\ns-ks-_ksdevice_dispatch.md">KSDEVICE_DISPATCH</a>



<a href="..\ks\nf-ks-ksinitializedriver.md">KsInitializeDriver</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSDEVICE_DESCRIPTOR structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>