---
UID : NC:wdm.GET_SET_DEVICE_DATA
title : GET_SET_DEVICE_DATA
author : windows-driver-content
description : The GetBusData routine reads data from the device's configuration space.
old-location : kernel\getbusdata.htm
old-project : kernel
ms.assetid : F5BDB3DF-6AC9-424E-BC69-27071F3D3820
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : kernel.getbusdata, GetBusData routine [Kernel-Mode Driver Architecture], GetBusData, GET_SET_DEVICE_DATA, GET_SET_DEVICE_DATA, wdm/GetBusData, kernel.busgetdevicedata, drvr_interface_f4fd2eab-5924-4ffa-b39e-fd7e0f74e5df.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : wdm.h
req.include-header : Ntddk.h
req.target-type : Desktop
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
req.irql : See Remarks section.
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PWDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME"
req.product : Windows 10 or later.
---


# GET_SET_DEVICE_DATA function
The <i>GetBusData</i> routine reads data from the device's configuration space.

## Syntax

```
GET_SET_DEVICE_DATA GetSetDeviceData;

_IRQL_requires_same_ ULONG GetSetDeviceData(
  PVOID Context,
  ULONG DataType,
  PVOID Buffer,
  ULONG Offset,
  ULONG Length
)
{...}
```

## Parameters

`Context`

A pointer to interface-specific context information. The caller passes the value that is passed as the <b>Context</b> member of the <a href="..\wdm\ns-wdm-_bus_interface_standard.md">BUS_INTERFACE_STANDARD</a> structure for the interface.

`DataType`

The type of bus data to read. For more information, see the discussion of the <i>WhichSpace</i> parameter in <a href="https://msdn.microsoft.com/library/windows/hardware/ff551727">IRP_MN_READ_CONFIG</a>.

`Buffer`

A pointer to the buffer that holds the configuration information to be read from the device's configuration space.

`Offset`

The offset into the bus-specific device data where this read operation begins. For example, if the <i>DataType</i> parameter is <b>PCI_WHICHSPACE_CONFIG</b>, the <i>Offset</i> parameter value is the offset into PCI Configuration Space.

`Length`

The length, in bytes, of data to read.


## Return Value

The <i>GetBusData</i> routine returns the length, in bytes, of the configuration data that is read after a successful read operation. If the read operation is unsuccessful, a value of zero is returned.

## Remarks

Depending on the value of the <i>DataType</i> parameter, the <i>GetBusData</i> routine can be called only from the interrupt request levels (IRQLs) that are defined in the following table.
<table>
<tr>
<th><i>DataType</i> value</th>
<th>IRQL</th>
</tr>
<tr>
<td>
<b>PCI_WHICHSPACE_CONFIG</b>

</td>
<td>
&lt;= DIRQL

</td>
</tr>
<tr>
<td>
<b>PCI_WHICHSPACE_ROM </b>

</td>
<td>
&lt;= APC_LEVEL

</td>
</tr>
<tr>
<td>
<b>PCCARD_COMMON_MEMORY</b>

<b>PCCARD_COMMON_MEMORY_INDIRECT</b>

</td>
<td>
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<td>
<b>PCCARD_ATTRIBUTE_MEMORY</b>

<b>PCCARD_ATTRIBUTE_MEMORY_INDIRECT</b>

</td>
<td>
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<td>
<b>PCCARD_PCI_CONFIGURATION_SPACE</b>

</td>
<td>
&lt;= DIRQL

</td>
</tr>
</table> 

The following remarks apply to drivers for PCI Express (PCIe) virtual functions (VFs) on devices that support the single root I/O virtualization (SR-IOV) interface:
<ul>
<li>
Drivers for PCIe VFs should call the <i>GetBusData</i> routine at IRQL &lt;= APC_LEVEL.

</li>
<li>
In order to read PCI Configuration data for the VF at IRQL = DISPATCH_LEVEL, the driver must issue I/O requests of <a href="https://msdn.microsoft.com/library/windows/hardware/ff551727">IRP_MN_READ_CONFIG</a>.

</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Ntddk.h) |
| **Library** |  |
| **IRQL** | See Remarks section. |
| **DDI compliance rules** |  |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551727">IRP_MN_READ_CONFIG</a>

<a href="..\wdm\ns-wdm-_bus_interface_standard.md">BUS_INTERFACE_STANDARD</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20GET_SET_DEVICE_DATA routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>