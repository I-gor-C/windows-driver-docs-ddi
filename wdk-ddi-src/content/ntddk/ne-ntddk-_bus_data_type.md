---
UID: NE:ntddk._BUS_DATA_TYPE
title: "_BUS_DATA_TYPE"
author: windows-driver-content
description: The BUS_DATA_TYPE enumeration indicates the type of bus configuration space.
old-location: kernel\bus_data_type.htm
old-project: kernel
ms.assetid: a2a2e964-b9ae-4367-85de-f0ebe3c7a952
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: "*PBUS_DATA_TYPE, BUS_DATA_TYPE, BUS_DATA_TYPE enumeration [Kernel-Mode Driver Architecture], CbusConfiguration, Cmos, ConfigurationSpaceUndefined, EisaConfiguration, MPIConfiguration, MPSAConfiguration, MaximumBusDataType, NuBusConfiguration, PBUS_DATA_TYPE, PBUS_DATA_TYPE enumeration pointer [Kernel-Mode Driver Architecture], PCIConfiguration, PCMCIAConfiguration, PNPISAConfiguration, Pos, SgiInternalConfiguration, VMEConfiguration, _BUS_DATA_TYPE, kernel.bus_data_type, ntddk/BUS_DATA_TYPE, ntddk/CbusConfiguration, ntddk/Cmos, ntddk/ConfigurationSpaceUndefined, ntddk/EisaConfiguration, ntddk/MPIConfiguration, ntddk/MPSAConfiguration, ntddk/MaximumBusDataType, ntddk/NuBusConfiguration, ntddk/PBUS_DATA_TYPE, ntddk/PCIConfiguration, ntddk/PCMCIAConfiguration, ntddk/PNPISAConfiguration, ntddk/Pos, ntddk/SgiInternalConfiguration, ntddk/VMEConfiguration, sysenum_3f6df31a-39d8-463e-8d44-44e51cd9989d.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddk.h
req.include-header: Ntddk.h, Miniport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddk.h
api_name:
-	BUS_DATA_TYPE
product: Windows
targetos: Windows
req.typenames: BUS_DATA_TYPE, *PBUS_DATA_TYPE
---

# _BUS_DATA_TYPE Enumeration
The <b>BUS_DATA_TYPE</b> enumeration indicates the type of bus configuration space.

## Syntax
````
typedef enum _BUS_DATA_TYPE { 
  ConfigurationSpaceUndefined  = -1,
  Cmos                         = 0,
  EisaConfiguration            = 1,
  Pos                          = 2,
  CbusConfiguration            = 3,
  PCIConfiguration             = 4,
  VMEConfiguration             = 5,
  NuBusConfiguration           = 6,
  PCMCIAConfiguration          = 7,
  MPIConfiguration             = 8,
  MPSAConfiguration            = 9,
  PNPISAConfiguration          = 10,
  SgiInternalConfiguration     = 11,
  MaximumBusDataType           = 12
} BUS_DATA_TYPE, *PBUS_DATA_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>ConfigurationSpaceUndefined</td>
                    <td>Indicates that the type of bus configuration space is undefined.</td>
                </tr>
            
                <tr>
                    <td>Cmos</td>
                    <td>Indicates CMOS data.</td>
                </tr>
            
                <tr>
                    <td>EisaConfiguration</td>
                    <td>Indicates an EISA bus configuration space.</td>
                </tr>
            
                <tr>
                    <td>Pos</td>
                    <td>For internal use only.</td>
                </tr>
            
                <tr>
                    <td>CbusConfiguration</td>
                    <td>Indicates Cbus configuration space.</td>
                </tr>
            
                <tr>
                    <td>PCIConfiguration</td>
                    <td>Indicates PCI configuration space.</td>
                </tr>
            
                <tr>
                    <td>VMEConfiguration</td>
                    <td>Indicates VME configuration space.</td>
                </tr>
            
                <tr>
                    <td>NuBusConfiguration</td>
                    <td>Indicates NuBus configuration space.</td>
                </tr>
            
                <tr>
                    <td>PCMCIAConfiguration</td>
                    <td>Indicates PCMCIA configuration space.</td>
                </tr>
            
                <tr>
                    <td>MPIConfiguration</td>
                    <td>Indicates MPI configuration space.</td>
                </tr>
            
                <tr>
                    <td>MPSAConfiguration</td>
                    <td>Indicates MPSA configuration space.</td>
                </tr>
            
                <tr>
                    <td>PNPISAConfiguration</td>
                    <td>Indicates PNPISA configuration space.</td>
                </tr>
            
                <tr>
                    <td>SgiInternalConfiguration</td>
                    <td>Indicates SGI internal bus configuration space.</td>
                </tr>
            
                <tr>
                    <td>MaximumBusDataType</td>
                    <td>Indicates the upper limit of the bus configuration space types.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddk.h (include Ntddk.h, Miniport.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546599">HalGetBusData</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546628">HalSetBusData</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546606">HalGetBusDataByOffset</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546633">HalSetBusDataByOffset</a>