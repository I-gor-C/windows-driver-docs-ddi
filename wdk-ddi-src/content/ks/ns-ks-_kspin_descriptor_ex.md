---
UID: NS:ks._KSPIN_DESCRIPTOR_EX
title: "_KSPIN_DESCRIPTOR_EX"
author: windows-driver-content
description: The KSPIN_DESCRIPTOR_EX structure describes the characteristics of a pin type on a given filter type.
old-location: stream\kspin_descriptor_ex.htm
old-project: stream
ms.assetid: 05c82973-86f9-44f9-8df2-1fc84c8be975
ms.author: windowsdriverdev
ms.date: 1/9/2018
ms.keywords: KSPIN_FLAG_HYPERCRITICAL_PROCESSING, ks/KSPIN_DESCRIPTOR_EX, KSPIN_FLAG_FIXED_FORMAT, _KSPIN_DESCRIPTOR_EX, KSPIN_FLAG_GENERATE_MAPPINGS, *PKSPIN_DESCRIPTOR_EX, KSPIN_FLAG_DISTINCT_TRAILING_EDGE, KSPIN_FLAG_FRAMES_NOT_REQUIRED_FOR_PROCESSING, KSPIN_FLAG_GENERATE_EOS_EVENTS, KSPIN_DESCRIPTOR_EX, KSPIN_FLAG_DISPATCH_LEVEL_PROCESSING, PKSPIN_DESCRIPTOR_EX structure pointer [Streaming Media Devices], KSPIN_FLAG_INITIATE_PROCESSING_ON_EVERY_ARRIVAL, stream.kspin_descriptor_ex, avstruct_6a73afe1-d131-47fc-877b-1abff4a75833.xml, KSPIN_FLAG_ENFORCE_FIFO, KSPIN_FLAG_PROCESS_IF_ANY_IN_RUN_STATE, KSPIN_DESCRIPTOR_EX structure [Streaming Media Devices], KSPIN_FLAG_IMPLEMENT_CLOCK, KSPIN_FLAG_PROCESS_IN_RUN_STATE_ONLY, KSPIN_FLAG_ASYNCHRONOUS_PROCESSING, KSPIN_FLAG_DENY_USERMODE_ACCESS, KSPIN_FLAG_CRITICAL_PROCESSING, ks/PKSPIN_DESCRIPTOR_EX, KSPIN_FLAG_SPLITTER, KSPIN_FLAG_SOME_FRAMES_REQUIRED_FOR_PROCESSING, KSPIN_FLAG_USE_STANDARD_TRANSPORT, KSPIN_FLAG_RENDERER, PKSPIN_DESCRIPTOR_EX, KSPIN_FLAG_DO_NOT_INITIATE_PROCESSING, KSPIN_FLAG_DO_NOT_USE_STANDARD_TRANSPORT
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
-	KSPIN_DESCRIPTOR_EX
product: Windows
targetos: Windows
req.typenames: KSPIN_DESCRIPTOR_EX, *PKSPIN_DESCRIPTOR_EX
---

# _KSPIN_DESCRIPTOR_EX structure
The KSPIN_DESCRIPTOR_EX structure describes the characteristics of a pin type on a given filter type.

## Syntax
````
typedef struct _KSPIN_DESCRIPTOR_EX {
  const KSPIN_DISPATCH         *Dispatch;
  const KSAUTOMATION_TABLE     *AutomationTable;
  KSPIN_DESCRIPTOR             PinDescriptor;
  ULONG                        Flags;
  ULONG                        InstancesPossible;
  ULONG                        InstancesNecessary;
  const KSALLOCATOR_FRAMING_EX *AllocatorFraming;
  PFNKSINTERSECTHANDLEREX      IntersectHandler;
} KSPIN_DESCRIPTOR_EX, *PKSPIN_DESCRIPTOR_EX;
````

## Members


## Remarks
<div class="alert"><b>Note</b>    AMCap and Blink might not be able to find tuner and crossbar interfaces on your AVStream driver if the <b>InstancesNecessary</b> member of KSPIN_DESCRIPTOR_EX is set to zero for the analog video input pin. To fix this problem, set <b>InstancesNecessary</b> for this pin to one.</div><div> </div>Note that the allocator framing requirements of your pin may be ignored despite the fact that your allocator framing specifies that alignment or size is absolutely required to be a certain value. If your kernel-mode driver is connected to an upstream user-mode filter that allocates for it and the particular upstream filter's allocator does not understand framing requirements, this can happen (current particular examples include the MPEG-2 splitter).

Furthermore, if you specify KSPIN_FLAG_DO_NOT_INITIATE_PROCESSING and the pin uses the standard transport mechanism, you must have a processing object. This means there must be some process dispatch provided (either at the filter level or at the pin level); even if this function is never called, it must be provided in this circumstance.


<a href="https://msdn.microsoft.com/44281574-8258-47a3-857d-fd44bb949f17">Data Range Intersections in AVStream</a> and <a href="https://msdn.microsoft.com/c2cfc183-0f4c-4104-a580-234e0483eee4">AVStream Splitters</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions. Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions. |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="..\ks\ns-ks-_kspin_dispatch.md">KSPIN_DISPATCH</a>

<a href="..\ks\ns-ks-kspin_descriptor.md">KSPIN_DESCRIPTOR</a>

<a href="..\ks\ns-ks-ksallocator_framing_ex.md">KSALLOCATOR_FRAMING_EX</a>

<a href="..\ks\nf-ks-ksdeviceregisteradapterobject.md">KsDeviceRegisterAdapterObject</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPIN_DESCRIPTOR_EX structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>