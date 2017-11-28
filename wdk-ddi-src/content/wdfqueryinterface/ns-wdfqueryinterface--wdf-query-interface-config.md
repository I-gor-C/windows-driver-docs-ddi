---
UID: NS.wdfqueryinterface._WDF_QUERY_INTERFACE_CONFIG
title: WDF_QUERY_INTERFACE_CONFIG
author: windows-driver-content
description: The WDF_QUERY_INTERFACE_CONFIG structure describes a driver-defined interface.
old-location: wdf\wdf_query_interface_config.htm
old-project: wdf
ms.assetid: 2f7112fc-7f3e-415d-9994-ffd93f456d97
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_QUERY_INTERFACE_CONFIG, WDF_QUERY_INTERFACE_CONFIG, *PWDF_QUERY_INTERFACE_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfqueryinterface.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_QUERY_INTERFACE_CONFIG
req.alt-loc: Wdfqueryinterface.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# WDF_QUERY_INTERFACE_CONFIG structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_QUERY_INTERFACE_CONFIG</b> structure describes a driver-defined interface.</p>


## -syntax

````
typedef struct _WDF_QUERY_INTERFACE_CONFIG {
  ULONG                                          Size;
  PINTERFACE                                     Interface;
  const GUID                                     *InterfaceType;
  BOOLEAN                                        SendQueryToParentStack;
  PFN_WDF_DEVICE_PROCESS_QUERY_INTERFACE_REQUEST EvtDeviceProcessQueryInterfaceRequest;
  BOOLEAN                                        ImportInterface;
} WDF_QUERY_INTERFACE_CONFIG, *PWDF_QUERY_INTERFACE_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>Interface</b>

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a> structure that describes the driver-defined interface. </p>
</dd>

### -field <b>InterfaceType</b>

<dd>
<p>A pointer to the GUID that identifies the interface.</p>
</dd>

### -field <b>SendQueryToParentStack</b>

<dd>
<p>If <b>TRUE</b>, and if your driver specifies a device object that represents a physical device object (PDO) when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545870">WdfDeviceAddQueryInterface</a>, the framework sends requests for the interface to the top of the parent device's driver stack. If this member is <b>FALSE</b>, or if the device object does not represent a PDO, the framework does not send requests to the parent device's stack. For more information, see the following Remarks section.</p>
</dd>

### -field <b>EvtDeviceProcessQueryInterfaceRequest</b>

<dd>
<p>A pointer to your driver's <a href="wdf.evtdeviceprocessqueryinterfacerequest">EvtDeviceProcessQueryInterfaceRequest</a> event callback function, which is called when another driver requests the interface.</p>
</dd>

### -field <b>ImportInterface</b>

<dd>
<p>If <b>TRUE</b>, the interface supports two-way communication between your driver and drivers that request the interface. </p>
<p>If this member is <b>FALSE</b>, the interface supports one-way communication from your driver to drivers that request the interface. </p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_QUERY_INTERFACE_CONFIG</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545870">WdfDeviceAddQueryInterface</a> method. </p>

<p>For each driver-defined interface that your driver exports, you must allocate a WDF_QUERY_INTERFACE_CONFIG structure that represents the interface. Other drivers can request access to the interface by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547289">WdfFdoQueryForInterface</a>. </p>

<p>If you want your interface to support two-way communication between the requesting driver and your driver, set the <b>ImportInterface</b> member to <b>TRUE</b>. If <b>ImportInterface</b> is <b>TRUE</b>, the structure that is provided by the requesting driver can contain data that your driver can read. In this case:</p>

<p>The <a href="wdf.evtdeviceprocessqueryinterfacerequest">EvtDeviceProcessQueryInterfaceRequest</a> callback function is required, and it must initialize the interface structure that the requesting driver provides. </p>

<p>Because the <a href="wdf.evtdeviceprocessqueryinterfacerequest">EvtDeviceProcessQueryInterfaceRequest</a> callback function provides the interface to the requesting driver, the <b>Interface</b> member of <b>WDF_QUERY_INTERFACE_CONFIG</b> can be <b>NULL</b>. If you provide a non-<b>NULL</b> pointer, the framework verifies that the size and version values that the requesting driver supplies are equal to or less than the values in your <a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a> structure. If either of these values are greater, the framework rejects the request. If you do not provide a value for <b>Interface</b>, your <i>EvtDeviceProcessQueryInterfaceRequest</i> callback function must verify those values.</p>

<p>If you want your interface to support only one-way communication from your driver to the requesting driver, set <b>ImportInterface</b> is <b>FALSE</b>. The interface structure that the requesting driver provides can receive only data that your driver provides. In this case:</p>

<p>The <a href="wdf.evtdeviceprocessqueryinterfacerequest">EvtDeviceProcessQueryInterfaceRequest</a> callback function is optional.</p>

<p>The <b>Interface</b> member cannot be <b>NULL</b>. The framework verifies that the GUID, size, and version values that the requesting driver supplies match the ones you supplied, and the framework rejects the request if the values do not match. If the values are valid, the framework initializes the interface structure that the requesting driver provides by using values the you supply for <b>Interface</b>.</p>

<p>Additionally, the <b>Interface</b> member can be <b>NULL</b> if the value of the <b>SendQueryToParentStack</b> member is <b>TRUE</b>. </p>

<p>If the <b>Interface</b> member is non-<b>NULL</b>, the framework copies the value to internal storage space. Therefore, the driver can allocate the INTERFACE structure in local, temporary storage space.</p>

<p>When your driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545870">WdfDeviceAddQueryInterface</a>, it can associate the interface with a framework device object that represents either a functional device object (FDO) or a physical device object (PDO). If the driver associates the interface with a PDO, it can set the <b>SendQueryToParentStack</b> member of the <b>WDF_QUERY_INTERFACE_CONFIG</b> structure to <b>TRUE</b>. When the framework intercepts a request for the interface, it checks the <b>SendQueryToParentStack</b> member and, if it is set to <b>TRUE</b>, the framework sends the request to the top of the driver stack of the PDO's parent. As a result, the request travels down two driver stacks: first, the stack that contains the driver that is requesting the interface and, second, the stack of the parent of the interface's device.</p>

<p>The framework provides two reference/dereference methods that you can use with your interfaces by specifying their addresses for the <b>InterfaceReference</b> and <b>InterfaceDereference</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a> structure. For more information about these methods, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546796">WdfDeviceInterfaceReferenceNoOp</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff546790">WdfDeviceInterfaceDereferenceNoOp</a>.</p>

<p>Drivers should initialize this structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff552443">WDF_QUERY_INTERFACE_CONFIG_INIT</a>.</p>

<p>For more information about driver-defined interfaces, see <a href="wdf.using_driver_defined_interfaces">Using Driver-Defined Interfaces</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfqueryinterface.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.evtdeviceprocessqueryinterfacerequest">EvtDeviceProcessQueryInterfaceRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552443">WDF_QUERY_INTERFACE_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545870">WdfDeviceAddQueryInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546796">WdfDeviceInterfaceReferenceNoOp</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546790">WdfDeviceInterfaceDereferenceNoOp</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547289">WdfFdoQueryForInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_QUERY_INTERFACE_CONFIG structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
