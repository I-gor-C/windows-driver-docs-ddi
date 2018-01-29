---
UID : NS:d3dkmthk._D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE
title : _D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE
author : windows-driver-content
description : A structure holding information to submit a signal to the hardware queue.
old-location : display\d3dkmt_submitsignalsyncobjectstohwqueue.htm
old-project : display
ms.assetid : BD192367-4960-4FD9-867F-02263AC93A61
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE, _D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE, D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE structure [Display Devices], display.d3dkmt_submitsignalsyncobjectstohwqueue, d3dkmthk/D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmthk.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
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
req.typenames : D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE
---

# _D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE structure
A structure holding information to submit a signal to the hardware queue.

## Syntax
````
typedef struct _D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE {
  D3DDDICB_SIGNALFLAGS Flags;
  ULONG                BroadcastHwQueueCount;
  const D3DKMT_HANDLE  *BroadcastHwQueueArray;
  UINT                 ObjectCount;
  const D3DKMT_HANDLE  *ObjectHandleArray;
  const UINT64         *FenceValueArray;
} D3DKMT_SUBMITSIGNALSYNCOBJECTSTOHWQUEUE;
````

## Members


`BroadcastHwQueueArray`

Specifies hardware queue handles to broadcast to.

`BroadcastHwQueueCount`

Specifies the number of hardware queues to broadcast this signal to.

`FenceValueArray`

Monitored fence values to signal.

`Flags`

Flags that specify signal behavior.

`ObjectCount`

Number of objects to signal.

`ObjectHandleArray`

Handles to monitored fence synchronization objects to signal.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmthk.h |