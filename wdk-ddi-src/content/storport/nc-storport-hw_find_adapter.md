---
UID: NC.storport.HW_FIND_ADAPTER
title: HW_FIND_ADAPTER
author: windows-driver-content
description: The HwStorFindAdapter routine uses the supplied configuration to determine whether a specific HBA is supported and, if it is, to return configuration information about that adapter.
old-location: storage\hwstorfindadapter.htm
old-project: storage
ms.assetid: 8642d0b8-ebc8-4053-b35e-3a81108a2f7f
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _STORAGE_DEVICE_UNIQUE_IDENTIFIER, STORAGE_DEVICE_UNIQUE_IDENTIFIER, *PSTORAGE_DEVICE_UNIQUE_IDENTIFIER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HwStorFindAdapter
req.alt-loc: Storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (See Remarks section.)
req.product: Windows 10 or later.
---

# HW_FIND_ADAPTER callback



## -description
The <b>HwStorFindAdapter</b> routine uses the supplied configuration to determine whether a specific HBA is supported and, if it is, to return configuration information about that adapter.


## -prototype

````
HW_FIND_ADAPTER HwStorFindAdapter;

ULONG HwStorFindAdapter(
          IN PVOID                        DeviceExtension,
  _In_    PVOID                           HwContext,
  _In_    PVOID                           BusInformation,
  _In_    IN PVOID                        ArgumentString,
  _Inout_ PPORT_CONFIGURATION_INFORMATION ConfigInfo,
  _In_    PBOOLEAN                        Reserved3
)
{ ... }
````


## -parameters

### -param DeviceExtension 

Supplies a per adapter storage area.

### -param HwContext [in]

Set to NULL.

### -param BusInformation [in]

Set to NULL.

### -param ArgumentString [in]

Supplies a <b>NULL</b>-terminated string with context information about the driver.

### -param ConfigInfo [in, out]

Supplies an initialized <a href="storage.port_configuration_information__storport_">PORT_CONFIGURATION_INFORMATION</a> structure that the miniport driver uses during initialization.

### -param Reserved3 [in]

Reserved for system use. 

## -returns
<b>HwStorFindAdapter</b> must return one of the following status values:
<dl>
<dt><b>SP_RETURN_FOUND</b></dt>
</dl>Indicates that a supported HBA was found and that the HBA-relevant configuration information was successfully determined and set in the <a href="storage.port_configuration_information__storport_">PORT_CONFIGURATION_INFORMATION</a> structure.
<dl>
<dt><b>SP_RETURN_ERROR</b></dt>
</dl>Indicates that an HBA was found but there was an error obtaining the configuration information. If possible, such an error should be logged with <a href="storage.storportlogerror">StorPortLogError</a>.
<dl>
<dt><b>SP_RETURN_BAD_CONFIG</b></dt>
</dl>Indicates that the supplied configuration information was invalid for the adapter.
<dl>
<dt><b>SP_RETURN_NOT_FOUND</b></dt>
</dl>Indicates that no supported HBA was found for the supplied configuration information.

 

## -remarks
Because the Storport driver supports only Plug and Play (PnP) devices, the <i>HwContext</i> and <i>BusInformation</i> parameters to <b>HwStorFindAdapter</b> are not supplied to non-virtual miniport drivers.

<b>HwStorFindAdapter</b> must set the <b>MaximumTransferLength</b> and <b>NumberOfPhysicalBreaks</b> fields in the <i>ConfigInfo</i> structure. Other than these fields, the <a href="storage.port_configuration_information__storport_">PORT_CONFIGURATION_INFORMATION</a> structure will always fully specify all adapter resources that are required to start the adapter. 

The name <b>HwStorFindAdapter</b> is just a placeholder. The actual prototype of this routine is defined in <i>Storport.h</i> as follows:

In most cases StorPort calls the <b>HwStorFindAdapter</b> routine at IRQL == PASSIVE_LEVEL without acquiring any spin locks. The exception case is when the miniport does not support calling <a href="storage.hwstoradaptercontrol">HwStorAdaptorControl</a> with the <b>ScsiRestartAdapter</b> control type. In this situation, StorPort will instead reinitialize the adapter by calling both  <b>HwStorFindAdapter</b> and <a href="storage.hwstorinitialize">HwStorInitialize</a>. When this is the case, <b>HwStorFindAdapter</b> is called at IRQL == DISPATCH_LEVEL. Also, when in dump mode, <b>HwStorFindAdapter</b> is called at IRQL == HIGH_LEVEL.

To define an <b>HwStorFindAdapter</b> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.

 For example, to define a <b>HwStorFindAdapter</b> callback routine that is named <i>MyHwFindAdapter</i>, use the <b>HW_FIND_ADAPTER</b> type as shown in this code example:

Then, implement your callback routine as follows:

The <b>HW_FIND_ADAPTER</b> function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>HW_FIND_ADAPTER</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/40BD11CD-A559-4F90-BF39-4ED2FB800392">Declaring Functions Using Function Role Types for Storport Drivers</a>. For information about _Use_decl_annotations_, see <a href="c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.

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
Header
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL (See Remarks section.)
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.port_configuration_information__storport_">PORT_CONFIGURATION_INFORMATION</a>
</dt>
<dt>
<a href="storage.storportlogerror">StorPortLogError</a>
</dt>
<dt>
<a href="storage.storportinitialize">StorPortInitialize</a>
</dt>
<dt>
<a href="storage.hwstorinitialize">HwStorInitialize</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HwStorFindAdapter routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
