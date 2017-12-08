---
UID: NS.USBCAMDI._USBCAMD_DEVICE_DATA
title: _USBCAMD_DEVICE_DATA
author: windows-driver-content
description: This structure is obsolete and is provided to maintain backward compatibility with the original USBCAMD.
old-location: stream\usbcamd_device_data.htm
old-project: stream
ms.assetid: 1841be02-e30f-4685-82ea-2d9c02ce7277
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _USBCAMD_DEVICE_DATA, USBCAMD_DEVICE_DATA, *PUSBCAMD_DEVICE_DATA
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
req.product: Windows 10 or later.
---

# _USBCAMD_DEVICE_DATA structure



## -description
This structure is <b>obsolete</b> and is provided to maintain backward compatibility with the original USBCAMD. New camera minidrivers should use the <a href="stream.usbcamd_device_data2">USBCAMD_DEVICE_DATA2</a> structure.
The USBCAMD_DEVICE_DATA structure specifies the entry points for a camera minidriver's functions that the original USBCAMD calls.


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

### -field Sig

Reserved. Do not use.

### -field CamInitialize

Pointer to the camera minidriver defined <a href="stream.caminitialize">CamInitialize</a> callback function. This entry point is required.

### -field CamUnInitialize

Pointer to the camera minidriver defined <a href="stream.camuninitialize">CamUnInitialize</a> callback function. This entry point is required.

### -field CamProcessUSBPacket

Pointer to the camera minidriver defined <a href="stream.camprocessusbpacket">CamProcessUSBPacket</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

### -field CamNewVideoFrame

Pointer to the camera minidriver defined <a href="stream.camnewvideoframe">CamNewVideoFrame</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

### -field CamProcessRawVideoFrame

Pointer to the camera minidriver defined <a href="stream.camprocessrawvideoframe">CamProcessRawVideoFrame</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

### -field CamStartCapture

Pointer to the camera minidriver defined <a href="stream.camstartcapture">CamStartCapture</a> callback function. This entry point is required.

### -field CamStopCapture

Pointer to the camera minidriver defined <a href="stream.camstopcapture">CamStopCapture</a> callback function. This entry point is required.

### -field CamConfigure

Pointer to the camera minidriver defined <a href="stream.camconfigure">CamConfigure</a> callback function. This entry point is required.

### -field CamSaveState

Pointer to the camera minidriver defined <a href="stream.camsavestate">CamSaveState</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

### -field CamRestoreState

Pointer to the camera minidriver defined <a href="stream.camrestorestate">CamRestoreState</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

### -field CamAllocateBandwidth

Pointer to the camera minidriver defined <a href="stream.camallocatebandwidth">CamAllocateBandwidth</a> callback function. This entry point is required.

### -field CamFreeBandwidth

Pointer to the camera minidriver defined <a href="stream.camfreebandwidth">CamFreeBandwidth</a> callback function. This entry point is required.

## -remarks
A camera minidriver passes a USBCAMD_DEVICE_DATA structure to USBCAMD as a parameter to the USBCAMD library routine <a href="stream.usbcamd_adapterreceivepacket">USBCAMD_AdapterReceivePacket</a> in the original USBCAMD.

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
<a href="stream.usbcamd_device_data2">USBCAMD_DEVICE_DATA2</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20USBCAMD_DEVICE_DATA structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
