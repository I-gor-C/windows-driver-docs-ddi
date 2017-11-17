---
UID: NS.usbcamdi._USBCAMD_DEVICE_DATA2
title: USBCAMD_DEVICE_DATA2
author: windows-driver-content
description: The USBCAMD_DEVICE_DATA2 structure specifies the entry points for a camera minidriver's functions that USBCAMD calls.
old-location: stream\usbcamd_device_data2.htm
ms.assetid: 51339fd1-a962-4e3c-b9c9-5fe54ff53aa0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: usbcamdi.h
req.include-header: Usbcamdi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBCAMD_DEVICE_DATA2
req.alt-loc: usbcamdi.h
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
ms.keywords: USBCAMD_DEVICE_DATA2, USBCAMD_DEVICE_DATA2, *PUSBCAMD_DEVICE_DATA2
req.iface: 
req.product: Windows 10 or later.
---

# USBCAMD_DEVICE_DATA2 structure



## -description
<p>The USBCAMD_DEVICE_DATA2 structure specifies the entry points for a camera minidriver's functions that USBCAMD calls.</p>


## -syntax

````
typedef struct _USBCAMD_DEVICE_DATA2 {
  ULONG                             Sig;
  PCAM_INITIALIZE_ROUTINE           CamInitialize;
  PCAM_INITIALIZE_ROUTINE           CamUnInitialize;
  PCAM_PROCESS_PACKET_ROUTINE_EX    CamProcessUSBPacketEx;
  PCAM_NEW_FRAME_ROUTINE_EX         CamNewVideoFrameEx;
  PCAM_PROCESS_RAW_FRAME_ROUTINE_EX CamProcessRawVideoFrameEx;
  PCAM_START_CAPTURE_ROUTINE_EX     CamStartCaptureEx;
  PCAM_STOP_CAPTURE_ROUTINE_EX      CamStopCaptureEx;
  PCAM_CONFIGURE_ROUTINE_EX         CamConfigureEx;
  PCAM_STATE_ROUTINE                CamSaveState;
  PCAM_STATE_ROUTINE                CamRestoreState;
  PCAM_ALLOCATE_BW_ROUTINE_EX       CamAllocateBandwidthEx;
  PCAM_FREE_BW_ROUTINE_EX           CamFreeBandwidthEx;
} USBCAMD_DEVICE_DATA2, *PUSBCAMD_DEVICE_DATA2;
````


## -struct-fields
<dl>

### -field <b>Sig</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>CamInitialize</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557614">CamInitialize</a> callback function. This entry point is required.</p>
</dd>

### -field <b>CamUnInitialize</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557646">CamUnInitialize</a> callback function. This entry point is required.</p>
</dd>

### -field <b>CamProcessUSBPacketEx</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557631">CamProcessUSBPacketEx</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.</p>
</dd>

### -field <b>CamNewVideoFrameEx</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557620">CamNewVideoFrameEx</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.</p>
</dd>

### -field <b>CamProcessRawVideoFrameEx</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557625">CamProcessRawVideoFrameEx</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.</p>
</dd>

### -field <b>CamStartCaptureEx</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557640">CamStartCaptureEx</a> callback function. This entry point is required.</p>
</dd>

### -field <b>CamStopCaptureEx</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557643">CamStopCaptureEx</a> callback function. This entry point is required.</p>
</dd>

### -field <b>CamConfigureEx</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557605">CamConfigureEx</a> callback function. This entry point is required.</p>
</dd>

### -field <b>CamSaveState</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557635">CamSaveState</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.</p>
</dd>

### -field <b>CamRestoreState</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557633">CamRestoreState</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.</p>
</dd>

### -field <b>CamAllocateBandwidthEx</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557600">CamAllocateBandwidthEx</a> callback function. This entry point is required.</p>
</dd>

### -field <b>CamFreeBandwidthEx</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557613">CamFreeBandwidthEx</a> callback function. This entry point is required.</p>
</dd>
</dl>

## -remarks
<p>A camera minidriver passes a USBCAMD_DEVICE_DATA2 structure to USBCAMD as a parameter to USBCAMD service <a href="https://msdn.microsoft.com/library/windows/hardware/ff568599">USBCAMD_InitializeNewInterface</a>.</p>

<p>Camera minidrivers that must be backward compatible with the original USBCAMD library must use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568585">USBCAMD_DEVICE_DATA</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbcamdi.h (include Usbcamdi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568599">USBCAMD_InitializeNewInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557614">CamInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557646">CamUnInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557631">CamProcessUSBPacketEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557620">CamNewVideoFrameEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557625">CamProcessRawVideoFrameEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557640">CamStartCaptureEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557643">CamStopCaptureEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557605">CamConfigureEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557635">CamSaveState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557633">CamRestoreState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557600">CamAllocateBandwidthEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557613">CamFreeBandwidthEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20USBCAMD_DEVICE_DATA2 structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
