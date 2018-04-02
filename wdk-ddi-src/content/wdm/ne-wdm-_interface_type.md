---
UID: NE:wdm._INTERFACE_TYPE
title: "_INTERFACE_TYPE"
author: windows-driver-content
description: The INTERFACE_TYPE enumeration indicates the bus type.
old-location: kernel\interface_type.htm
old-project: kernel
ms.assetid: 4d20f3fd-d06e-420b-af69-9ef34addc611
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PINTERFACE_TYPE, ACPIBus, CBus, Eisa, INTERFACE_TYPE, INTERFACE_TYPE enumeration [Kernel-Mode Driver Architecture], InterfaceTypeUndefined, Internal, InternalPowerBus, Isa, MPIBus, MPSABus, MaximumInterfaceType, MicroChannel, NuBus, PCIBus, PCMCIABus, PINTERFACE_TYPE, PINTERFACE_TYPE enumeration pointer [Kernel-Mode Driver Architecture], PNPBus, PNPISABus, ProcessorInternal, TurboChannel, VMEBus, Vmcs, _INTERFACE_TYPE, kernel.interface_type, sysenum_a73e08e6-79ef-4a5b-82b1-cfd4bc4269f8.xml, wdm/ACPIBus, wdm/CBus, wdm/Eisa, wdm/INTERFACE_TYPE, wdm/InterfaceTypeUndefined, wdm/Internal, wdm/InternalPowerBus, wdm/Isa, wdm/MPIBus, wdm/MPSABus, wdm/MaximumInterfaceType, wdm/MicroChannel, wdm/NuBus, wdm/PCIBus, wdm/PCMCIABus, wdm/PINTERFACE_TYPE, wdm/PNPBus, wdm/PNPISABus, wdm/ProcessorInternal, wdm/TurboChannel, wdm/VMEBus, wdm/Vmcs"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Miniport.h, Wudfwdm.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wdm.h
api_name:
-	INTERFACE_TYPE
product: Windows
targetos: Windows
req.typenames: INTERFACE_TYPE, *PINTERFACE_TYPE
req.product: Windows 10 or later.
---

# _INTERFACE_TYPE Enumeration
The <b>INTERFACE_TYPE</b> enumeration indicates the bus type.

## Syntax
```
typedef enum _INTERFACE_TYPE {
  InterfaceTypeUndefined  ,
  Internal                ,
  Isa                     ,
  Eisa                    ,
  MicroChannel            ,
  TurboChannel            ,
  PCIBus                  ,
  VMEBus                  ,
  NuBus                   ,
  PCMCIABus               ,
  CBus                    ,
  MPIBus                  ,
  MPSABus                 ,
  ProcessorInternal       ,
  InternalPowerBus        ,
  PNPISABus               ,
  PNPBus                  ,
  Vmcs                    ,
  ACPIBus                 ,
  MaximumInterfaceType
} INTERFACE_TYPE, *PINTERFACE_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>InterfaceTypeUndefined</td>
                    <td>Indicates that the interface type is undefined.</td>
                </tr>
            
                <tr>
                    <td>Internal</td>
                    <td>For internal use only.</td>
                </tr>
            
                <tr>
                    <td>Isa</td>
                    <td>Indicates that the interface is published by the ISA bus driver.</td>
                </tr>
            
                <tr>
                    <td>Eisa</td>
                    <td>Indicates that the interface is published by the EISA bus driver.</td>
                </tr>
            
                <tr>
                    <td>MicroChannel</td>
                    <td>Indicates that the interface is published by the MicroChannel bus driver.</td>
                </tr>
            
                <tr>
                    <td>TurboChannel</td>
                    <td>Indicates that the interface is published by the TurboChannel bus driver.</td>
                </tr>
            
                <tr>
                    <td>PCIBus</td>
                    <td>Indicates that the interface is published by the PCI bus driver.</td>
                </tr>
            
                <tr>
                    <td>VMEBus</td>
                    <td>Indicates that the interface is published by the VME bus driver.</td>
                </tr>
            
                <tr>
                    <td>NuBus</td>
                    <td>Indicates that the interface is published by the NuBus driver.</td>
                </tr>
            
                <tr>
                    <td>PCMCIABus</td>
                    <td>Indicates that the interface is published by the PCMCIA bus driver.</td>
                </tr>
            
                <tr>
                    <td>CBus</td>
                    <td>Indicates that the interface is published by the Cbus driver.</td>
                </tr>
            
                <tr>
                    <td>MPIBus</td>
                    <td>Indicates that the interface is published by the MPI bus driver.</td>
                </tr>
            
                <tr>
                    <td>MPSABus</td>
                    <td>Indicates that the interface is published by the MPSA bus driver.</td>
                </tr>
            
                <tr>
                    <td>ProcessorInternal</td>
                    <td>Indicates that the interface is published by the ISA bus driver.</td>
                </tr>
            
                <tr>
                    <td>InternalPowerBus</td>
                    <td>Indicates that the interface is published for an internal power bus. Some devices have power control ports that allow them to share power control with other devices. The Windows architecture represents these devices as slots on a virtual bus called an "internal power bus."</td>
                </tr>
            
                <tr>
                    <td>PNPISABus</td>
                    <td>Indicates that the interface is published by the PNPISA bus driver.</td>
                </tr>
            
                <tr>
                    <td>PNPBus</td>
                    <td>Indicates that the interface is published by the PNP bus driver.</td>
                </tr>
            
                <tr>
                    <td>Vmcs</td>
                    <td>Reserved for use by the operating system.</td>
                </tr>
            
                <tr>
                    <td>ACPIBus</td>
                    <td>Indicates that the interface is published by the ACPI bus driver. The ACPI bus driver enumerates devices that are described in the ACPI firmware of the hardware platform. These devices might physically reside on buses that are controlled by other bus drivers, but the ACPI bus driver must enumerate these devices because the other bus drivers cannot detect them. This interface type is defined starting with Windows 8.</td>
                </tr>
            
                <tr>
                    <td>MaximumInterfaceType</td>
                    <td>Marks the upper limit of the possible bus types.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Miniport.h, Wudfwdm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff559682">HW_INITIALIZATION_DATA</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567785">PORT_CONFIGURATION_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff564629">ScsiPortGetDeviceBase</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff564761">ScsiPortValidateRange</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567080">StorPortGetDeviceBase</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567513">StorPortValidateRange</a>