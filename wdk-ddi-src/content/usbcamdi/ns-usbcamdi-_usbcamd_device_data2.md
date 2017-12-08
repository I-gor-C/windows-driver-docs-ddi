---
UID: NS.USBCAMDI._USBCAMD_DEVICE_DATA2
title: _USBCAMD_DEVICE_DATA2
author: windows-driver-content
description: The USBCAMD_DEVICE_DATA2 structure specifies the entry points for a camera minidriver's functions that USBCAMD calls.
old-location: stream\usbcamd_device_data2.htm
old-project: stream
ms.assetid: 51339fd1-a962-4e3c-b9c9-5fe54ff53aa0
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _USBCAMD_DEVICE_DATA2, *PUSBCAMD_DEVICE_DATA2, USBCAMD_DEVICE_DATA2
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
req.product: Windows 10 or later.
---

# _USBCAMD_DEVICE_DATA2 structure



## -description
The USBCAMD_DEVICE_DATA2 structure specifies the entry points for a camera minidriver's functions that USBCAMD calls.


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

### -field Sig

Reserved. Do not use.

### -field CamInitialize

Pointer to the camera minidriver defined <a href="stream.caminitialize">CamInitialize</a> callback function. This entry point is required.

### -field CamUnInitialize

Pointer to the camera minidriver defined <a href="stream.camuninitialize">CamUnInitialize</a> callback function. This entry point is required.

### -field CamProcessUSBPacketEx

Pointer to the camera minidriver defined <a href="stream.camprocessusbpacketex">CamProcessUSBPacketEx</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

### -field CamNewVideoFrameEx

Pointer to the camera minidriver defined <a href="stream.camnewvideoframeex">CamNewVideoFrameEx</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

### -field CamProcessRawVideoFrameEx

Pointer to the camera minidriver defined <a href="stream.camprocessrawvideoframeex">CamProcessRawVideoFrameEx</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

### -field CamStartCaptureEx

Pointer to the camera minidriver defined <a href="stream.camstartcaptureex">CamStartCaptureEx</a> callback function. This entry point is required.

### -field CamStopCaptureEx

Pointer to the camera minidriver defined <a href="stream.camstopcaptureex">CamStopCaptureEx</a> callback function. This entry point is required.

### -field CamConfigureEx

Pointer to the camera minidriver defined <a href="stream.camconfigureex">CamConfigureEx</a> callback function. This entry point is required.

### -field CamSaveState

Pointer to the camera minidriver defined <a href="stream.camsavestate">CamSaveState</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

### -field CamRestoreState

Pointer to the camera minidriver defined <a href="stream.camrestorestate">CamRestoreState</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

### -field CamAllocateBandwidthEx

Pointer to the camera minidriver defined <a href="stream.camallocatebandwidthex">CamAllocateBandwidthEx</a> callback function. This entry point is required.

### -field CamFreeBandwidthEx

Pointer to the camera minidriver defined <a href="stream.camfreebandwidthex">CamFreeBandwidthEx</a> callback function. This entry point is required.

## -remarks
A camera minidriver passes a USBCAMD_DEVICE_DATA2 structure to USBCAMD as a parameter to USBCAMD service <a href="stream.usbcamd_initializenewinterface">USBCAMD_InitializeNewInterface</a>.

Camera minidrivers that must be backward compatible with the original USBCAMD library must use the <a href="stream.usbcamd_device_data">USBCAMD_DEVICE_DATA</a> structure.

## -requirements
<table>
<tr>
<th width="30%">
Header
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
<a href="stream.usbcamd_initializenewinterface">USBCAMD_InitializeNewInterface</a>
</dt>
<dt>
<a href="stream.caminitialize">CamInitialize</a>
</dt>
<dt>
<a href="stream.camuninitialize">CamUnInitialize</a>
</dt>
<dt>
<a href="stream.camprocessusbpacketex">CamProcessUSBPacketEx</a>
</dt>
<dt>
<a href="stream.camnewvideoframeex">CamNewVideoFrameEx</a>
</dt>
<dt>
<a href="stream.camprocessrawvideoframeex">CamProcessRawVideoFrameEx</a>
</dt>
<dt>
<a href="stream.camstartcaptureex">CamStartCaptureEx</a>
</dt>
<dt>
<a href="stream.camstopcaptureex">CamStopCaptureEx</a>
</dt>
<dt>
<a href="stream.camconfigureex">CamConfigureEx</a>
</dt>
<dt>
<a href="stream.camsavestate">CamSaveState</a>
</dt>
<dt>
<a href="stream.camrestorestate">CamRestoreState</a>
</dt>
<dt>
<a href="stream.camallocatebandwidthex">CamAllocateBandwidthEx</a>
</dt>
<dt>
<a href="stream.camfreebandwidthex">CamFreeBandwidthEx</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20USBCAMD_DEVICE_DATA2 structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
