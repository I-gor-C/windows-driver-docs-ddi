---
UID: NS:usbcamdi._USBCAMD_DEVICE_DATA2
title: "_USBCAMD_DEVICE_DATA2"
author: windows-driver-content
description: The USBCAMD_DEVICE_DATA2 structure specifies the entry points for a camera minidriver's functions that USBCAMD calls.
old-location: stream\usbcamd_device_data2.htm
old-project: stream
ms.assetid: 51339fd1-a962-4e3c-b9c9-5fe54ff53aa0
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PUSBCAMD_DEVICE_DATA2, PUSBCAMD_DEVICE_DATA2, PUSBCAMD_DEVICE_DATA2 structure pointer [Streaming Media Devices], USBCAMD_DEVICE_DATA2, USBCAMD_DEVICE_DATA2 structure [Streaming Media Devices], _USBCAMD_DEVICE_DATA2, stream.usbcamd_device_data2, usbcamdi/PUSBCAMD_DEVICE_DATA2, usbcamdi/USBCAMD_DEVICE_DATA2, usbcmdpr_01305731-bde1-4718-8ff9-d0f102d6cc34.xml"
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
-	usbcamdi.h
api_name:
-	USBCAMD_DEVICE_DATA2
product:
- Windows
targetos: Windows
req.typenames: USBCAMD_DEVICE_DATA2, *PUSBCAMD_DEVICE_DATA2
req.product: Windows 10 or later.
---

# _USBCAMD_DEVICE_DATA2 structure
The USBCAMD_DEVICE_DATA2 structure specifies the entry points for a camera minidriver's functions that USBCAMD calls.

## Syntax
```
typedef struct _USBCAMD_DEVICE_DATA2 {
  ULONG                             Sig;
  PCAM_INITIALIZE_ROUTINE           CamInitialize;
  PCAM_INITIALIZE_ROUTINE           CamUnInitialize;
  PCAM_PROCESS_PACKET_ROUTINE_EX    CamProcessUSBPacketEx;
  PCAM_NEW_FRAME_ROUTINE_EX         CamNewVideoFrameEx;
  PCAM_PROCESS_RAW_FRAME_ROUTINE_EX CamProcessRawVideoFrameEx;
  PCAM_START_CAPTURE_ROUTINE_EX     CamStartCaptureEx;
  PCAM_STOP_CAPTURE_ROUTINE_EX      CamStopCaptureEx;
  PCAM_CONFIGURE_ROUTINE_EX         CamConfigureEx;
  PCAM_STATE_ROUTINE                CamSaveState;
  PCAM_STATE_ROUTINE                CamRestoreState;
  PCAM_ALLOCATE_BW_ROUTINE_EX       CamAllocateBandwidthEx;
  PCAM_FREE_BW_ROUTINE_EX           CamFreeBandwidthEx;
} *PUSBCAMD_DEVICE_DATA2, USBCAMD_DEVICE_DATA2;
```

## Members


`Sig`

Reserved. Do not use.

`CamInitialize`

Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557614">CamInitialize</a> callback function. This entry point is required.

`CamUnInitialize`

Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557646">CamUnInitialize</a> callback function. This entry point is required.

`CamProcessUSBPacketEx`

Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557631">CamProcessUSBPacketEx</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

`CamNewVideoFrameEx`

Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557620">CamNewVideoFrameEx</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

`CamProcessRawVideoFrameEx`

Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557625">CamProcessRawVideoFrameEx</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

`CamStartCaptureEx`

Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557640">CamStartCaptureEx</a> callback function. This entry point is required.

`CamStopCaptureEx`

Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557643">CamStopCaptureEx</a> callback function. This entry point is required.

`CamConfigureEx`

Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557605">CamConfigureEx</a> callback function. This entry point is required.

`CamSaveState`

Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557635">CamSaveState</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

`CamRestoreState`

Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557633">CamRestoreState</a> callback function. This is an optional entry point. If the minidriver does not implement this function, it must point to an empty function.

`CamAllocateBandwidthEx`

Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557600">CamAllocateBandwidthEx</a> callback function. This entry point is required.

`CamFreeBandwidthEx`

Pointer to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557613">CamFreeBandwidthEx</a> callback function. This entry point is required.

## Remarks
A camera minidriver passes a USBCAMD_DEVICE_DATA2 structure to USBCAMD as a parameter to USBCAMD service <a href="https://msdn.microsoft.com/library/windows/hardware/ff568599">USBCAMD_InitializeNewInterface</a>.

Camera minidrivers that must be backward compatible with the original USBCAMD library must use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568585">USBCAMD_DEVICE_DATA</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbcamdi.h (include Usbcamdi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557600">CamAllocateBandwidthEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557605">CamConfigureEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557613">CamFreeBandwidthEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557614">CamInitialize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557620">CamNewVideoFrameEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557625">CamProcessRawVideoFrameEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557631">CamProcessUSBPacketEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557633">CamRestoreState</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557635">CamSaveState</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557640">CamStartCaptureEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557643">CamStopCaptureEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557646">CamUnInitialize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568599">USBCAMD_InitializeNewInterface</a>