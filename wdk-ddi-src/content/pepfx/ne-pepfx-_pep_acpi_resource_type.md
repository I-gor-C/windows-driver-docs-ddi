---
UID: NE:pepfx._PEP_ACPI_RESOURCE_TYPE
title: "_PEP_ACPI_RESOURCE_TYPE"
author: windows-driver-content
description: The PEP_ACPI_RESOURCE_TYPE enumeration is used to identify the type of ACPI resource that is contained in the PEP_ACPI_RESOURCE union.
old-location: kernel\pep_acpi_resource_type.htm
old-project: kernel
ms.assetid: C67FA5DF-D2E4-4F00-B22F-9218F0012708
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: PEP_ACPI_RESOURCE_TYPE, PEP_ACPI_RESOURCE_TYPE enumeration [Kernel-Mode Driver Architecture], PepAcpiExtendedIo, PepAcpiExtendedMemory, PepAcpiGpioInt, PepAcpiGpioIo, PepAcpiInterrupt, PepAcpiIoPort, PepAcpiMemory, PepAcpiSpbI2c, PepAcpiSpbSpi, PepAcpiSpbUart, _PEP_ACPI_RESOURCE_TYPE, kernel.pep_acpi_resource_type, pepfx/PEP_ACPI_RESOURCE_TYPE, pepfx/PepAcpiExtendedIo, pepfx/PepAcpiExtendedMemory, pepfx/PepAcpiGpioInt, pepfx/PepAcpiGpioIo, pepfx/PepAcpiInterrupt, pepfx/PepAcpiIoPort, pepfx/PepAcpiMemory, pepfx/PepAcpiSpbI2c, pepfx/PepAcpiSpbSpi, pepfx/PepAcpiSpbUart
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: pepfx.h
req.include-header: Pep_x.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
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
-	pepfx.h
api_name:
-	PEP_ACPI_RESOURCE_TYPE
product:
- Windows
targetos: Windows
req.typenames: PEP_ACPI_RESOURCE_TYPE
---

# _PEP_ACPI_RESOURCE_TYPE Enumeration
The <b>PEP_ACPI_RESOURCE_TYPE</b> enumeration is used to identify the type of ACPI resource that is contained in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186691">PEP_ACPI_RESOURCE</a> union.

## Syntax
```
typedef enum _PEP_ACPI_RESOURCE_TYPE {
  PepAcpiMemory          ,
  PepAcpiIoPort          ,
  PepAcpiInterrupt       ,
  PepAcpiGpioIo          ,
  PepAcpiGpioInt         ,
  PepAcpiSpbI2c          ,
  PepAcpiSpbSpi          ,
  PepAcpiSpbUart         ,
  PepAcpiExtendedMemory  ,
  PepAcpiExtendedIo
} PEP_ACPI_RESOURCE_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>PepAcpiMemory</td>
                    <td>Indicates that the resource is an ACPI memory resource.</td>
                </tr>
            
                <tr>
                    <td>PepAcpiIoPort</td>
                    <td>Indicates that the resource is an ACPI IO port resource.</td>
                </tr>
            
                <tr>
                    <td>PepAcpiInterrupt</td>
                    <td>Indicates that the resource is an ACPI interrupt resource.</td>
                </tr>
            
                <tr>
                    <td>PepAcpiGpioIo</td>
                    <td>Indicates that the resource is an ACPI GPIO resource.</td>
                </tr>
            
                <tr>
                    <td>PepAcpiGpioInt</td>
                    <td>Indicates that the resource is an ACPI GPIO interrupt resource.</td>
                </tr>
            
                <tr>
                    <td>PepAcpiSpbI2c</td>
                    <td>Indicates that the resource is an ACPI I2C serial bus resource.</td>
                </tr>
            
                <tr>
                    <td>PepAcpiSpbSpi</td>
                    <td>Indicates that the resource is an ACPI SPI serial bus resource.</td>
                </tr>
            
                <tr>
                    <td>PepAcpiSpbUart</td>
                    <td>Indicates that the resource is an ACPI UART serial bus resource.</td>
                </tr>
            
                <tr>
                    <td>PepAcpiExtendedMemory</td>
                    <td>Indicates that the resource is an ACPI extended memory resource.</td>
                </tr>
            
                <tr>
                    <td>PepAcpiExtendedIo</td>
                    <td>Indicates that the resource is an ACPI extended IO resource.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pepfx.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt186690">PEP_ACPI_REQUEST_CONVERT_TO_BIOS_RESOURCES</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt186691">PEP_ACPI_RESOURCE</a>