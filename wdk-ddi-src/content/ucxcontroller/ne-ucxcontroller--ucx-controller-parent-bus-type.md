---
UID: NE.ucxcontroller._UCX_CONTROLLER_PARENT_BUS_TYPE
title: UCX_CONTROLLER_PARENT_BUS_TYPE
author: windows-driver-content
description: The UCX_CONTROLLER_PARENT_BUS_TYPE enumeration defines the parent bus type.
old-location: buses\ucx_controller_parent_bus_type.htm
old-project: usbref
ms.assetid: FD78074D-E128-4085-A178-0133C9256E42
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCM_PD_REQUEST_DATA_OBJECT, UCM_PD_REQUEST_DATA_OBJECT, *PUCM_PD_REQUEST_DATA_OBJECT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ucxcontroller.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UCX_CONTROLLER_PARENT_BUS_TYPE
req.alt-loc: Ucxcontroller.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UCX_CONTROLLER_PARENT_BUS_TYPE enumeration



## -description
<p>The <b>UCX_CONTROLLER_PARENT_BUS_TYPE</b> enumeration defines the parent bus type.</p>


## -syntax

````
typedef enum _UCX_CONTROLLER_PARENT_BUS_TYPE { 
  UcxControllerParentBusTypeCustom,
  UcxControllerParentBusTypePci,
  UcxControllerParentBusTypeAcpi
} UCX_CONTROLLER_PARENT_BUS_TYPE;
````


## -enum-fields
<dl>

### -field <a id="UcxControllerParentBusTypeCustom"></a><a id="ucxcontrollerparentbustypecustom"></a><a id="UCXCONTROLLERPARENTBUSTYPECUSTOM"></a><b>UcxControllerParentBusTypeCustom</b>

<dd>
<p>Custom bus type.</p>
</dd>

### -field <a id="UcxControllerParentBusTypePci"></a><a id="ucxcontrollerparentbustypepci"></a><a id="UCXCONTROLLERPARENTBUSTYPEPCI"></a><b>UcxControllerParentBusTypePci</b>

<dd>
<p>Parent bus is PCI.</p>
</dd>

### -field <a id="UcxControllerParentBusTypeAcpi"></a><a id="ucxcontrollerparentbustypeacpi"></a><a id="UCXCONTROLLERPARENTBUSTYPEACPI"></a><b>UcxControllerParentBusTypeAcpi</b>

<dd>
<p>Parent is ACPI.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucxcontroller.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt188057">UCX_CONTROLLER_CONFIG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UCX_CONTROLLER_PARENT_BUS_TYPE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
