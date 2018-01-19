---
UID : NE:d3dukmdt._D3DDDI_SYNCHRONIZATIONOBJECT_TYPE
title : _D3DDDI_SYNCHRONIZATIONOBJECT_TYPE
author : windows-driver-content
description : The D3DDDI_SYNCHRONIZATIONOBJECT_TYPE enumeration indicates the type of synchronization object.
old-location : display\d3dddi_synchronizationobject_type.htm
old-project : display
ms.assetid : afd1aad4-d4cd-420f-bd3f-f171dc818a3e
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3DDDI_SYNCHRONIZATIONOBJECT_TYPE, D3DDDI_SYNCHRONIZATIONOBJECT_TYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dukmdt.h
req.include-header : D3dukmdt.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DDDI_SYNCHRONIZATIONOBJECT_TYPE
req.alt-loc : d3dukmdt.h
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
req.typenames : D3DDDI_SYNCHRONIZATIONOBJECT_TYPE
---

# _D3DDDI_SYNCHRONIZATIONOBJECT_TYPE Enumeration
The <b>D3DDDI_SYNCHRONIZATIONOBJECT_TYPE</b> enumeration indicates the type of synchronization object.

## Syntax
````
typedef enum _D3DDDI_SYNCHRONIZATIONOBJECT_TYPE { 
  D3DDDI_SYNCHRONIZATION_MUTEX  = 1,
  D3DDDI_SEMAPHORE              = 2,
  D3DDDI_FENCE                  = 3,
  D3DDDI_CPU_NOTIFICATION       = 4,
#if ((DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0) || \
     (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM2_0))
  D3DDDI_MONITORED_FENCE        = 5,
#endif 
#if ((DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0) || \
     (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM2_0))
  D3DDDI_MONITORED_FENCE        = 6,
#endif 
  
} D3DDDI_SYNCHRONIZATIONOBJECT_TYPE;
````

## Constants

<table>

<tr>
<td>D3DDDI_CPU_NOTIFICATION</td>
<td>The synchronization object is a CPU notification.

Supported starting with Windows 7.</td>
</tr>

<tr>
<td>D3DDDI_FENCE</td>
<td>The synchronization object is a fence. 

Supported starting with Windows 7.</td>
</tr>

<tr>
<td>D3DDDI_MONITORED_FENCE</td>
<td>The synchronization object is a monitored fence.

Supported starting with Windows 10.</td>
</tr>

<tr>
<td>D3DDDI_SEMAPHORE</td>
<td>The synchronization object is a semaphore.

Supported starting with Windows Vista.</td>
</tr>

<tr>
<td>D3DDDI_SYNCHRONIZATION_MUTEX</td>
<td>The synchronization object is a synchronization mutex.

Supported starting with Windows Vista.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dukmdt.h (include D3dukmdt.h) |