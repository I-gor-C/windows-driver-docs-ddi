---
UID: NF:wdfqueryinterface.WdfDeviceInterfaceReferenceNoOp
title: WdfDeviceInterfaceReferenceNoOp function
author: windows-driver-content
description: The WdfDeviceInterfaceReferenceNoOp method can be used for driver-defined interfaces that do not require reference counts.
old-location: wdf\wdfdeviceinterfacereferencenoop.htm
old-project: wdf
ms.assetid: 9bb18fd3-e803-4f51-822e-88c06d3385cc
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: WdfDeviceInterfaceReferenceNoOp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfqueryinterface.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDeviceInterfaceReferenceNoOp
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: Any level
req.typenames: WDF_PDO_EVENT_CALLBACKS, *PWDF_PDO_EVENT_CALLBACKS
req.product: Windows 10 or later.
---

# WdfDeviceInterfaceReferenceNoOp function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDeviceInterfaceReferenceNoOp</b> method can be used for driver-defined interfaces that do not require reference counts.



## -syntax

````
VOID WdfDeviceInterfaceReferenceNoOp(
  _In_ PVOID Context
);
````


## -parameters

### -param Context [in]

This parameter is not used.


## -returns
None


## -remarks
You can use the <b>WdfDeviceInterfaceReferenceNoOp</b> method's address as the <b>InterfaceReference</b> member of the <a href="..\wdm\ns-wdm-_interface.md">INTERFACE</a> structure that is contained in the framework's <a href="..\wdfqueryinterface\ns-wdfqueryinterface-_wdf_query_interface_config.md">WDF_QUERY_INTERFACE_CONFIG</a> structure.

For more information about interface reference counts and the <b>WdfDeviceInterfaceReferenceNoOp</b> method, see <a href="https://msdn.microsoft.com/ad96add6-c982-429b-b815-d7adf6fed8cc">Using Driver-Defined Interfaces</a>.

For a code example that uses <b>WdfDeviceInterfaceReferenceNoOp</b>, see <a href="..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceaddqueryinterface.md">WdfDeviceAddQueryInterface</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfqueryinterface.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="https://msdn.microsoft.com/51db6f3c-45cb-46a7-9dd4-2bab67893fea">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm-_interface.md">INTERFACE</a>
</dt>
<dt>
<a href="..\wdfqueryinterface\ns-wdfqueryinterface-_wdf_query_interface_config.md">WDF_QUERY_INTERFACE_CONFIG</a>
</dt>
<dt>
<a href="..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceinterfacedereferencenoop.md">WdfDeviceInterfaceDereferenceNoOp</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInterfaceReferenceNoOp method%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

