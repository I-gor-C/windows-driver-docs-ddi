---
UID: NS.hdaudio._HDAUDIO_BUS_INTERFACE
title: HDAUDIO_BUS_INTERFACE
author: windows-driver-content
description: The HDAUDIO_BUS_INTERFACE structure specifies the information that a client requires to call the routines in the HDAUDIO_BUS_INTERFACE version of the HD Audio DDI. Another variant of this DDI is specified by the HDAUDIO_BUS_INTERFACE_BDL structure.
old-location: audio\hdaudio_bus_interface.htm
ms.assetid: 6b3bc5ce-05d2-45e0-91d8-6bb34e58777f
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: hdaudio.h
req.include-header: Hdaudio.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HDAUDIO_BUS_INTERFACE
req.alt-loc: hdaudio.h
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
ms.keywords: HDAUDIO_BUS_INTERFACE, HDAUDIO_BUS_INTERFACE, *PHDAUDIO_BUS_INTERFACE
req.iface: 
---

# HDAUDIO_BUS_INTERFACE structure



## -description
<p>The HDAUDIO_BUS_INTERFACE structure specifies the information that a client requires to call the routines in the HDAUDIO_BUS_INTERFACE version of the HD Audio DDI. Another variant of this DDI is specified by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536416">HDAUDIO_BUS_INTERFACE_BDL</a> structure.</p>


## -syntax

````
typedef struct _HDAUDIO_BUS_INTERFACE {
  USHORT                       Size;
  USHORT                       Version;
  PVOID                        Context;
  PINTERFACE_REFERENCE         InterfaceReference;
  PINTERFACE_DEREFERENCE       InterfaceDereference;
  PTRANSFER_CODEC_VERBS        TransferCodecVerbs;
  PALLOCATE_CAPTURE_DMA_ENGINE AllocateCaptureDmaEngine;
  PALLOCATE_RENDER_DMA_ENGINE  AllocateRenderDmaEngine;
  PCHANGE_BANDWIDTH_ALLOCATION ChangeBandwidthAllocation;
  PALLOCATE_DMA_BUFFER         AllocateDmaBuffer;
  PFREE_DMA_BUFFER             FreeDmaBuffer;
  PFREE_DMA_ENGINE             FreeDmaEngine;
  PSET_DMA_ENGINE_STATE        SetDmaEngineState;
  PGET_WALL_CLOCK_REGISTER     GetWallClockRegister;
  PGET_LINK_POSITION_REGISTER  GetLinkPositionRegister;
  PREGISTER_EVENT_CALLBACK     RegisterEventCallback;
  PUNREGISTER_EVENT_CALLBACK   UnregisterEventCallback;
  PGET_DEVICE_INFORMATION      GetDeviceInformation;
  PGET_RESOURCE_INFORMATION    GetResourceInformation;
} HDAUDIO_BUS_INTERFACE, *PHDAUDIO_BUS_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size in bytes of the HDAUDIO_BUS_INTERFACE structure.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Specifies the version of the baseline HD Audio DDI.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>Pointer to interface-specific context information.</p>
</dd>

### -field <b>InterfaceReference</b>

<dd>
<p>Pointer to a driver-supplied routine that increments the interface's reference count.</p>
</dd>

### -field <b>InterfaceDereference</b>

<dd>
<p>Pointer to a driver-supplied routine that decrements the interface's reference count.</p>
</dd>

### -field <b>TransferCodecVerbs</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/0ba92f5c-c4a3-48de-b8af-9c444b2e65b5">TransferCodecVerbs</a> routine.</p>
</dd>

### -field <b>AllocateCaptureDmaEngine</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/038e52be-04db-41c2-aa19-85bc4eb8bc57">AllocateCaptureDmaEngine</a> routine.</p>
</dd>

### -field <b>AllocateRenderDmaEngine</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/fb2a64ca-7e8e-4352-86c6-b9500e535c75">AllocateRenderDmaEngine</a> routine.</p>
</dd>

### -field <b>ChangeBandwidthAllocation</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/4dcf8fb6-71f5-4e11-a92a-0292c2a1515c">ChangeBandwidthAllocation</a> routine.</p>
</dd>

### -field <b>AllocateDmaBuffer</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/44fd988a-24b3-4587-88d9-30585800ffbf">AllocateDmaBuffer</a> routine.</p>
</dd>

### -field <b>FreeDmaBuffer</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/658e32d2-40e2-4479-8212-df7140fe6b74">FreeDmaBuffer</a> routine.</p>
</dd>

### -field <b>FreeDmaEngine</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/3f068ac0-2b18-4242-86de-7044ce558788">FreeDmaEngine</a> routine.</p>
</dd>

### -field <b>SetDmaEngineState</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/05cfb827-e143-4d77-b378-e02dd381e429">SetDmaEngineState</a> routine.</p>
</dd>

### -field <b>GetWallClockRegister</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/4efe4b23-eb4f-4170-8d73-05cae2ba21c2">GetWallClockRegister</a> routine.</p>
</dd>

### -field <b>GetLinkPositionRegister</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/8b8c7f61-c22a-421f-999f-291999bb243f">GetLinkPositionRegister</a> routine.</p>
</dd>

### -field <b>RegisterEventCallback</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/0f94146b-aa60-4106-aba6-0f1cb3e53008">RegisterEventCallback</a> routine.</p>
</dd>

### -field <b>UnregisterEventCallback</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/698017a0-13d5-4ed5-a1ce-1a50a62135e0">UnregisterEventCallback</a> routine.</p>
</dd>

### -field <b>GetDeviceInformation</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/bdd08133-0641-4eea-bfa3-75f700356132">GetDeviceInformation</a> routine.</p>
</dd>

### -field <b>GetResourceInformation</b>

<dd>
<p>Function pointer to the <a href="https://msdn.microsoft.com/ba1f0fa2-77dd-4ec3-86c8-c5d74465743f">GetResourceInformation</a> routine.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> IOCTL uses this structure to provide interface information to a client that is querying the HD Audio bus driver for the HD Audio DDI. Another variant of this DDI is specified by the HDAUDIO_BUS_INTERFACE_BDL structure.</p>

<p>The HDAUDIO_BUS_INTERFACE and HDAUDIO_BUS_INTERFACE_BDL structures are similar but have the following differences:</p>

<p>HDAUDIO_BUS_INTERFACE has two members, <b>AllocateDmaBuffer</b> and <b>FreeDmaBuffer</b>, that are not present in HDAUDIO_BUS_INTERFACE_BDL.</p>

<p>HDAUDIO_BUS_INTERFACE_BDL has three members, <a href="https://msdn.microsoft.com/4538ce8e-fccd-4862-b226-a99fe578a5fd">AllocateContiguousDmaBuffer</a>, <a href="https://msdn.microsoft.com/7aaf98cc-8a94-44e6-9fef-76e00db17405">FreeContiguousDmaBuffer</a>, and <a href="https://msdn.microsoft.com/2760579b-9922-4709-a049-a73f3abd5043">SetupDmaEngineWithBdl</a>, that are not present in HDAUDIO_BUS_INTERFACE.</p>

<p>For more information, see <a href="NULL">Differences Between the HD Audio DDI Versions</a>.</p>

<p>The names and definitions of the first five members (<b>Size</b>, <b>Version</b>, <b>Context</b>, <b>InterfaceReference</b>, and <b>InterfaceDereference</b>) are the same as in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a> structure. The remaining members are specific to the baseline HD Audio DDI and specify function pointers to the routines in the DDI. For more information, see <a href="https://msdn.microsoft.com/78667254-62a6-41fe-af36-43dbdea63aa8">Obtaining an HDAUDIO_BUS_INTERFACE DDI Object</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hdaudio.h (include Hdaudio.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/0ba92f5c-c4a3-48de-b8af-9c444b2e65b5">TransferCodecVerbs</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/038e52be-04db-41c2-aa19-85bc4eb8bc57">AllocateCaptureDmaEngine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fb2a64ca-7e8e-4352-86c6-b9500e535c75">AllocateRenderDmaEngine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4dcf8fb6-71f5-4e11-a92a-0292c2a1515c">ChangeBandwidthAllocation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/44fd988a-24b3-4587-88d9-30585800ffbf">AllocateDmaBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/658e32d2-40e2-4479-8212-df7140fe6b74">FreeDmaBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3f068ac0-2b18-4242-86de-7044ce558788">FreeDmaEngine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/05cfb827-e143-4d77-b378-e02dd381e429">SetDmaEngineState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4efe4b23-eb4f-4170-8d73-05cae2ba21c2">GetWallClockRegister</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8b8c7f61-c22a-421f-999f-291999bb243f">GetLinkPositionRegister</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/0f94146b-aa60-4106-aba6-0f1cb3e53008">RegisterEventCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/698017a0-13d5-4ed5-a1ce-1a50a62135e0">UnregisterEventCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/bdd08133-0641-4eea-bfa3-75f700356132">GetDeviceInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ba1f0fa2-77dd-4ec3-86c8-c5d74465743f">GetResourceInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536416">HDAUDIO_BUS_INTERFACE_BDL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20HDAUDIO_BUS_INTERFACE structure%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
