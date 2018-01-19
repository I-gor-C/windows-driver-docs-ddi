---
UID : NS:d3dkmthk._D3DKMT_WAITFORVERTICALBLANKEVENT2
title : _D3DKMT_WAITFORVERTICALBLANKEVENT2
author : windows-driver-content
description : Describes parameters for multiple wait objects, including a vertical blank event. Supported starting with Windows 8.
old-location : display\d3dkmt_waitforverticalblankevent2.htm
old-project : display
ms.assetid : b83e1d1c-e940-4e7b-8a74-82aee2c54391
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3DKMT_WAITFORVERTICALBLANKEVENT2, D3DKMT_WAITFORVERTICALBLANKEVENT2
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmthk.h
req.include-header : D3dkmthk.h
req.target-type : Windows
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DKMT_WAITFORVERTICALBLANKEVENT2
req.alt-loc : D3dkmthk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : D3DKMT_WAITFORVERTICALBLANKEVENT2
---

# _D3DKMT_WAITFORVERTICALBLANKEVENT2 structure
Describes parameters for multiple wait objects, including a vertical blank event. Supported starting with Windows 8.

## Syntax
````
typedef struct _D3DKMT_WAITFORVERTICALBLANKEVENT2 {
  D3DKMT_HANDLE                  hAdapter;
  D3DKMT_HANDLE                  hDevice;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  UINT                           NumObjects;
  HANDLE                         ObjectHandleArray[D3DKMT_MAX_WAITFORVERTICALBLANK_OBJECTS];
} D3DKMT_WAITFORVERTICALBLANKEVENT2;
````

## Members

        
            `hAdapter`

            [in] A handle to the adapter.
        
            `hDevice`

            [in] A handle to the display device. This member is optionally specified. However, if the OpenGL ICD specifies the display device, the kernel is given more optimization opportunities with regard to power usage.
        
            `NumObjects`

            The number of wait objects to wait on, which equals the size of the array specified by the <b>ObjectHandleArray</b> member.
        
            `ObjectHandleArray`

            [in] A handle to an array of wait objects to wait on.
        
            `VidPnSourceId`

            [in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology for the VidPN source.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |