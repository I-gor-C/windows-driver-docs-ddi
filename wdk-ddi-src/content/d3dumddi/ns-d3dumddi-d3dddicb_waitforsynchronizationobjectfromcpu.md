---
UID : NS:d3dumddi.D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU
title : D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU
author : windows-driver-content
description : D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU is used with pfnWaitForSynchronizationObjectFromCpuCb to wait for a monitored fence to reach a certain value.
old-location : display\d3dddicb_waitforsynchronizationobjectfromcpu.htm
old-project : display
ms.assetid : 0F5BEDBF-6871-4343-88D1-85E7620171EF
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU, D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Windows
req.target-min-winverclnt : Windows 10
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU
req.alt-loc : d3dumddi.h
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
req.typenames : D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU
---

# D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU structure
<b>D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU</b> is used with <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_waitforsynchronizationobjectfromcpucb.md">pfnWaitForSynchronizationObjectFromCpuCb</a> to wait for a monitored fence to reach a certain value.

## Syntax
````
typedef struct D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU {
  UINT                                             ObjectCount;
  const D3DKMT_HANDLE                              *ObjectHandleArray;
  const UINT64                                     *FenceValueArray;
  HANDLE                                           hAsyncEvent;
  D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS Flags;
} D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU;
````

## Members

        
            `FenceValueArray`

            [in] An array of 64-bit monitored fence values to wait for, each corresponding to an object in the <b>ObjectHandleArray</b>.
        
            `Flags`

            [in] A <a href="..\d3dukmdt\ns-d3dukmdt-_d3dddi_waitforsynchronizationobjectfromcpu_flags.md">D3DDDI_WAITFORSYNCHRONIZATIONOBJECTFROMCPU_FLAGS</a> structure describing the operation.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `hAsyncEvent`

            [in] When not <b>NULL</b>, specifies the event to be signaled when the wait condition is satisfied. When <b>NULL</b>, the call will not return until the wait condition is satisfied.
        
            `ObjectCount`

            [in] The number of synchronization objects in the <b>ObjectHandleArray</b> and fence values in the <b>FenceValueArray</b>.
        
            `ObjectHandleArray`

            [in] An array of kernel-mode handles to the synchronization events to wait for.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |

    ## See Also

        <dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_waitforsynchronizationobjectfromcpucb.md">pfnWaitForSynchronizationObjectFromCpuCb</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_WAITFORSYNCHRONIZATIONOBJECTFROMCPU structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>