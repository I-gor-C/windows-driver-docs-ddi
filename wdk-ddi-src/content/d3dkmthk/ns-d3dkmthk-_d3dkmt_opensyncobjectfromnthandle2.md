---
UID : NS:d3dkmthk._D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2
title : "_D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2"
author : windows-driver-content
description : D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 is used with D3DKMTOpenSyncObjectFromNtHandle2 to open a monitored fence object.
old-location : display\d3dkmt_opensyncobjectfromnthandle2.htm
old-project : display
ms.assetid : 7C5F9ACF-AA21-4A2B-B943-3B1D940284E1
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : "_D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2, D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2, D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 structure [Display Devices], display.d3dkmt_opensyncobjectfromnthandle2, d3dkmthk/D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2"
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmthk.h
req.include-header : D3dkmthk.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2
---

# _D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 structure
<b>D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2</b> is used with <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtopensyncobjectfromnthandle2.md">D3DKMTOpenSyncObjectFromNtHandle2</a> to open a monitored fence object.

## Syntax
````
typedef struct _D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 {
  HANDLE                             hNtHandle;
  D3DKMT_HANDLE                      hDevice;
  D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS Flags;
  D3DKMT_HANDLE                      hSyncObject;
  union {
    struct {
      VOID                   *FenceValueCPUVirtualAddress;
      D3DGPU_VIRTUAL_ADDRESS FenceValueGPUVirtualAddress;
      UINT                   EngineAffinity;
    } MonitoredFence;
    UINT64 Reserved[8];
  };
} D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2;
````

## Members


`Flags`

[in] Specifies the desired sync object behavior for this device, such as wait and signal semantics and TDR handling.

`hDevice`

[in] Device handle to use this sync object on.

`hNtHandle`

[in] NT handle for the sync object to be opened.

`hSyncObject`

[out] Handle to the sync object that can be used in this process.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtopensyncobjectfromnthandle2.md">D3DKMTOpenSyncObjectFromNtHandle2</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>