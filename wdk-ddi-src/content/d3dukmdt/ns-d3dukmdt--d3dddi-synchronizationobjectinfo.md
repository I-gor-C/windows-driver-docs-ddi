---
UID: NS.d3dukmdt._D3DDDI_SYNCHRONIZATIONOBJECTINFO
title: D3DDDI_SYNCHRONIZATIONOBJECTINFO
author: windows-driver-content
description: The D3DDDI_SYNCHRONIZATIONOBJECTINFO structure contains information about a synchronization object.
old-location: display\d3dddi_synchronizationobjectinfo.htm
old-project: display
ms.assetid: 786934f5-b0ec-4ee9-8bf0-f32b64295b96
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_SYNCHRONIZATIONOBJECTINFO, D3DDDI_SYNCHRONIZATIONOBJECTINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_SYNCHRONIZATIONOBJECTINFO
req.alt-loc: d3dukmdt.h
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
---

# D3DDDI_SYNCHRONIZATIONOBJECTINFO structure



## -description
<p>The D3DDDI_SYNCHRONIZATIONOBJECTINFO structure contains information about a synchronization object.</p>


## -syntax

````
typedef struct _D3DDDI_SYNCHRONIZATIONOBJECTINFO {
  D3DDDI_SYNCHRONIZATIONOBJECT_TYPE Type;
  union {
    struct {
      BOOL InitialState;
    } SynchronizationMutex;
    struct {
      UINT MaxCount;
      UINT InitialCount;
    } Semaphore;
    struct {
      UINT Reserved[16];
    } Reserved;
  };
} D3DDDI_SYNCHRONIZATIONOBJECTINFO;
````


## -struct-fields
<dl>

### -field Type

<dd>
<p>[in] A <a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-synchronizationobject-type.md">D3DDDI_SYNCHRONIZATIONOBJECT_TYPE</a>-typed value that indicates the type of synchronization object.</p>
</dd>

### -field SynchronizationMutex

<dd>
<p>A structure that contains information about a synchronization mutex. If the <b>Type</b> member is equal to D3DDDI_SYNCHRONIZATION_MUTEX, the union in D3DDDI_SYNCHRONIZATIONOBJECTINFO holds a SynchronizationMutex structure, which contains the following member:</p>
<dl>

### -field InitialState

<dd>
<p>A Boolean value that indicates whether the synchronization mutex is initially owned by an object. A value of <b>TRUE</b> indicates that the mutex is owned; <b>FALSE</b> indicates that the mutex is not owned. </p>
</dd>
</dl>
</dd>

### -field Semaphore

<dd>
<p>A structure that contains information about a semaphore. If the <b>Type</b> member is equal to D3DDDI_SEMAPHORE, the union in D3DDDI_SYNCHRONIZATIONOBJECTINFO holds a Semaphore structure, which contains the following members:</p>
<dl>

### -field MaxCount

<dd>
<p>The maximum number of events that an object can be waiting for. </p>
</dd>

### -field InitialCount

<dd>
<p>The initial number of events that an object is waiting for. </p>
</dd>
</dl>
</dd>

### -field Reserved

<dd>
<p>A structure that is reserved for future use. This structure contains the following member:</p>
<dl>

### -field Reserved

<dd>
<p>An array of 32-bit values that are reserved for future use.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddi-synchronizationobject-type.md">D3DDDI_SYNCHRONIZATIONOBJECT_TYPE</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddicb-createsynchronizationobject.md">D3DDDICB_CREATESYNCHRONIZATIONOBJECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_SYNCHRONIZATIONOBJECTINFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
