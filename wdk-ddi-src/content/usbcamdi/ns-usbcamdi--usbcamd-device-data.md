---
UID: NS.usbcamdi._USBCAMD_DEVICE_DATA
title: USBCAMD_DEVICE_DATA
author: windows-driver-content
description: This structure is obsolete and is provided to maintain backward compatibility with the original USBCAMD.
old-location: stream\usbcamd_device_data.htm
old-project: stream
ms.assetid: 1841be02-e30f-4685-82ea-2d9c02ce7277
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: USBCAMD_DEVICE_DATA, USBCAMD_DEVICE_DATA, *PUSBCAMD_DEVICE_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbcamdi.h
req.include-header: Usbcamdi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBCAMD_DEVICE_DATA
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
req.iface: 
req.product: Windows 10 or later.
---

# USBCAMD_DEVICE_DATA structure



## -description
<p>This structure is <b>obsolete</b> and is provided to maintain backward compatibility with the original USBCAMD. New camera minidrivers should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568590">USBCAMD_DEVICE_DATA2</a> structure.</p>
<p>The USBCAMD_DEVICE_DATA structure specifies the entry points for a camera minidriver's functions that the original USBCAMD calls.</p>


## -syntax

````
typedef struct _USBCAMD_DEVICE_DATA {
  ULONG                          Sig;
  PCAM_INITIALIZE_ROUTINE        CamInitialize;
  PCAM_INITIALIZE_ROUTINE        CamUnInitialize;
  PCAM_PROCESS_PACKET_ROUTINE    CamProcessUSBPacket;
  PCAM_NEW_FRAME_ROUTINE         CamNewVideoFrame;
  PCAM_PROCESS_RAW_FRAME_ROUTINE CamProcessRawVideoFrame;
  PCAM_START_CAPTURE_ROUTINE     CamStartCapture;
  PCAM_STOP_CAPTURE_ROUTINE      CamStopCapture;
  PCAM_CONFIGURE_ROUTINE         CamConfigure;
  PCAM_STATE_ROUTINE             CamSaveState;
  PCAM_STATE_ROUTINE             CamRestoreState;
  PCAM_ALLOCATE_BW_ROUTINE       CamAllocateBandwidth;
  PCAM_FREE_BW_ROUTINE           CamFreeBandwidth;
} USBCAMD_DEVICE_DATA, *PUSBCAMD_DEVICE_DATA;
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

### -field <b>CamProcessUSBPacket</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557629">CamProcessUSBPacket</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.</p>
</dd>

### -field <b>CamNewVideoFrame</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557617">CamNewVideoFrame</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.</p>
</dd>

### -field <b>CamProcessRawVideoFrame</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557623">CamProcessRawVideoFrame</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.</p>
</dd>

### -field <b>CamStartCapture</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557637">CamStartCapture</a> callback function. This entry point is required.</p>
</dd>

### -field <b>CamStopCapture</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557642">CamStopCapture</a> callback function. This entry point is required.</p>
</dd>

### -field <b>CamConfigure</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557603">CamConfigure</a> callback function. This entry point is required.</p>
</dd>

### -field <b>CamSaveState</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557635">CamSaveState</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.</p>
</dd>

### -field <b>CamRestoreState</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557633">CamRestoreState</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.</p>
</dd>

### -field <b>CamAllocateBandwidth</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557595">CamAllocateBandwidth</a> callback function. This entry point is required.</p>
</dd>

### -field <b>CamFreeBandwidth</b>

<dd>
<p>Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557611">CamFreeBandwidth</a> callback function. This entry point is required.</p>
</dd>
</dl>

## -remarks
<p>A camera minidriver passes a USBCAMD_DEVICE_DATA structure to USBCAMD as a parameter to the USBCAMD library routine <a href="https://msdn.microsoft.com/library/windows/hardware/ff568574">USBCAMD_AdapterReceivePacket</a> in the original USBCAMD.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568590">USBCAMD_DEVICE_DATA2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20USBCAMD_DEVICE_DATA structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
