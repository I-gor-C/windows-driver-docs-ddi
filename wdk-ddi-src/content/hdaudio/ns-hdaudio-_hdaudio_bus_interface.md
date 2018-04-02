---
UID: NS:hdaudio._HDAUDIO_BUS_INTERFACE
title: "_HDAUDIO_BUS_INTERFACE"
author: windows-driver-content
description: The HDAUDIO_BUS_INTERFACE structure specifies the information that a client requires to call the routines in the HDAUDIO_BUS_INTERFACE version of the HD Audio DDI. Another variant of this DDI is specified by the HDAUDIO_BUS_INTERFACE_BDL structure.
old-location: audio\hdaudio_bus_interface.htm
old-project: audio
ms.assetid: 6b3bc5ce-05d2-45e0-91d8-6bb34e58777f
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: "*PHDAUDIO_BUS_INTERFACE, HDAUDIO_BUS_INTERFACE, HDAUDIO_BUS_INTERFACE structure [Audio Devices], PHDAUDIO_BUS_INTERFACE, PHDAUDIO_BUS_INTERFACE structure pointer [Audio Devices], _HDAUDIO_BUS_INTERFACE, aud-prop2_4d39bbd4-8c0b-4f2c-98a7-618d891593c1.xml, audio.hdaudio_bus_interface, hdaudio/HDAUDIO_BUS_INTERFACE, hdaudio/PHDAUDIO_BUS_INTERFACE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hdaudio.h
req.include-header: Hdaudio.h
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
req.irql: PASSIVE_LEVEL.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	hdaudio.h
api_name:
-	HDAUDIO_BUS_INTERFACE
product:
- Windows
targetos: Windows
req.typenames: HDAUDIO_BUS_INTERFACE, *PHDAUDIO_BUS_INTERFACE
---

# _HDAUDIO_BUS_INTERFACE structure
The HDAUDIO_BUS_INTERFACE structure specifies the information that a client requires to call the routines in the HDAUDIO_BUS_INTERFACE version of the HD Audio DDI. Another variant of this DDI is specified by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536416">HDAUDIO_BUS_INTERFACE_BDL</a> structure.

## Syntax
```
typedef struct _HDAUDIO_BUS_INTERFACE {
  USHORT                       Size;
  USHORT                       Version;
  PVOID                        Context;
  PINTERFACE_REFERENCE         InterfaceReference;
  PINTERFACE_DEREFERENCE       InterfaceDereference;
  PTRANSFER_CODEC_VERBS        TransferCodecVerbs;
  PALLOCATE_CAPTURE_DMA_ENGINE AllocateCaptureDmaEngine;
  PALLOCATE_RENDER_DMA_ENGINE  AllocateRenderDmaEngine;
  PCHANGE_BANDWIDTH_ALLOCATION ChangeBandwidthAllocation;
  PALLOCATE_DMA_BUFFER         AllocateDmaBuffer;
  PFREE_DMA_BUFFER             FreeDmaBuffer;
  PFREE_DMA_ENGINE             FreeDmaEngine;
  PSET_DMA_ENGINE_STATE        SetDmaEngineState;
  PGET_WALL_CLOCK_REGISTER     GetWallClockRegister;
  PGET_LINK_POSITION_REGISTER  GetLinkPositionRegister;
  PREGISTER_EVENT_CALLBACK     RegisterEventCallback;
  PUNREGISTER_EVENT_CALLBACK   UnregisterEventCallback;
  PGET_DEVICE_INFORMATION      GetDeviceInformation;
  PGET_RESOURCE_INFORMATION    GetResourceInformation;
} HDAUDIO_BUS_INTERFACE, *PHDAUDIO_BUS_INTERFACE;
```

## Members


`Size`

Specifies the size in bytes of the HDAUDIO_BUS_INTERFACE structure.

`Version`

Specifies the version of the baseline HD Audio DDI.

`Context`

Pointer to interface-specific context information.

`InterfaceReference`

Pointer to a driver-supplied routine that increments the interface's reference count.

`InterfaceDereference`

Pointer to a driver-supplied routine that decrements the interface's reference count.

`TransferCodecVerbs`

Function pointer to the <a href="https://msdn.microsoft.com/0ba92f5c-c4a3-48de-b8af-9c444b2e65b5">TransferCodecVerbs</a> routine.

`AllocateCaptureDmaEngine`

Function pointer to the <a href="https://msdn.microsoft.com/038e52be-04db-41c2-aa19-85bc4eb8bc57">AllocateCaptureDmaEngine</a> routine.

`AllocateRenderDmaEngine`

Function pointer to the <a href="https://msdn.microsoft.com/fb2a64ca-7e8e-4352-86c6-b9500e535c75">AllocateRenderDmaEngine</a> routine.

`ChangeBandwidthAllocation`

Function pointer to the <a href="https://msdn.microsoft.com/4dcf8fb6-71f5-4e11-a92a-0292c2a1515c">ChangeBandwidthAllocation</a> routine.

`AllocateDmaBuffer`

Function pointer to the <a href="https://msdn.microsoft.com/44fd988a-24b3-4587-88d9-30585800ffbf">AllocateDmaBuffer</a> routine.

`FreeDmaBuffer`

Function pointer to the <a href="https://msdn.microsoft.com/658e32d2-40e2-4479-8212-df7140fe6b74">FreeDmaBuffer</a> routine.

`FreeDmaEngine`

Function pointer to the <a href="https://msdn.microsoft.com/3f068ac0-2b18-4242-86de-7044ce558788">FreeDmaEngine</a> routine.

`SetDmaEngineState`

Function pointer to the <a href="https://msdn.microsoft.com/05cfb827-e143-4d77-b378-e02dd381e429">SetDmaEngineState</a> routine.

`GetWallClockRegister`

Function pointer to the <a href="https://msdn.microsoft.com/4efe4b23-eb4f-4170-8d73-05cae2ba21c2">GetWallClockRegister</a> routine.

`GetLinkPositionRegister`

Function pointer to the <a href="https://msdn.microsoft.com/8b8c7f61-c22a-421f-999f-291999bb243f">GetLinkPositionRegister</a> routine.

`RegisterEventCallback`

Function pointer to the <a href="https://msdn.microsoft.com/0f94146b-aa60-4106-aba6-0f1cb3e53008">RegisterEventCallback</a> routine.

`UnregisterEventCallback`

Function pointer to the <a href="https://msdn.microsoft.com/698017a0-13d5-4ed5-a1ce-1a50a62135e0">UnregisterEventCallback</a> routine.

`GetDeviceInformation`

Function pointer to the <a href="https://msdn.microsoft.com/bdd08133-0641-4eea-bfa3-75f700356132">GetDeviceInformation</a> routine.

`GetResourceInformation`

Function pointer to the <a href="https://msdn.microsoft.com/ba1f0fa2-77dd-4ec3-86c8-c5d74465743f">GetResourceInformation</a> routine.

## Remarks
The <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> IOCTL uses this structure to provide interface information to a client that is querying the HD Audio bus driver for the HD Audio DDI. Another variant of this DDI is specified by the HDAUDIO_BUS_INTERFACE_BDL structure.

The HDAUDIO_BUS_INTERFACE and HDAUDIO_BUS_INTERFACE_BDL structures are similar but have the following differences:

<ul>
<li>
HDAUDIO_BUS_INTERFACE has two members, <b>AllocateDmaBuffer</b> and <b>FreeDmaBuffer</b>, that are not present in HDAUDIO_BUS_INTERFACE_BDL.

</li>
<li>
HDAUDIO_BUS_INTERFACE_BDL has three members, <a href="https://msdn.microsoft.com/4538ce8e-fccd-4862-b226-a99fe578a5fd">AllocateContiguousDmaBuffer</a>, <a href="https://msdn.microsoft.com/7aaf98cc-8a94-44e6-9fef-76e00db17405">FreeContiguousDmaBuffer</a>, and <a href="https://msdn.microsoft.com/2760579b-9922-4709-a049-a73f3abd5043">SetupDmaEngineWithBdl</a>, that are not present in HDAUDIO_BUS_INTERFACE.

</li>
</ul>
For more information, see <a href="https://msdn.microsoft.com/e24071d3-9021-40c0-907a-91ada8a1306b">Differences Between the HD Audio DDI Versions</a>.

The names and definitions of the first five members (<b>Size</b>, <b>Version</b>, <b>Context</b>, <b>InterfaceReference</b>, and <b>InterfaceDereference</b>) are the same as in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a> structure. The remaining members are specific to the baseline HD Audio DDI and specify function pointers to the routines in the DDI. For more information, see <a href="https://msdn.microsoft.com/78667254-62a6-41fe-af36-43dbdea63aa8">Obtaining an HDAUDIO_BUS_INTERFACE DDI Object</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | hdaudio.h (include Hdaudio.h) |

## See Also

<a href="https://msdn.microsoft.com/038e52be-04db-41c2-aa19-85bc4eb8bc57">AllocateCaptureDmaEngine</a>



<a href="https://msdn.microsoft.com/44fd988a-24b3-4587-88d9-30585800ffbf">AllocateDmaBuffer</a>



<a href="https://msdn.microsoft.com/fb2a64ca-7e8e-4352-86c6-b9500e535c75">AllocateRenderDmaEngine</a>



<a href="https://msdn.microsoft.com/4dcf8fb6-71f5-4e11-a92a-0292c2a1515c">ChangeBandwidthAllocation</a>



<a href="https://msdn.microsoft.com/658e32d2-40e2-4479-8212-df7140fe6b74">FreeDmaBuffer</a>



<a href="https://msdn.microsoft.com/3f068ac0-2b18-4242-86de-7044ce558788">FreeDmaEngine</a>



<a href="https://msdn.microsoft.com/bdd08133-0641-4eea-bfa3-75f700356132">GetDeviceInformation</a>



<a href="https://msdn.microsoft.com/8b8c7f61-c22a-421f-999f-291999bb243f">GetLinkPositionRegister</a>



<a href="https://msdn.microsoft.com/ba1f0fa2-77dd-4ec3-86c8-c5d74465743f">GetResourceInformation</a>



<a href="https://msdn.microsoft.com/4efe4b23-eb4f-4170-8d73-05cae2ba21c2">GetWallClockRegister</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536416">HDAUDIO_BUS_INTERFACE_BDL</a>



<a href="https://msdn.microsoft.com/0f94146b-aa60-4106-aba6-0f1cb3e53008">RegisterEventCallback</a>



<a href="https://msdn.microsoft.com/05cfb827-e143-4d77-b378-e02dd381e429">SetDmaEngineState</a>



<a href="https://msdn.microsoft.com/0ba92f5c-c4a3-48de-b8af-9c444b2e65b5">TransferCodecVerbs</a>



<a href="https://msdn.microsoft.com/698017a0-13d5-4ed5-a1ce-1a50a62135e0">UnregisterEventCallback</a>