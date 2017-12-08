---
UID: NS.pepfx._PEP_ACPI_GPIO_RESOURCE
title: PEP_ACPI_GPIO_RESOURCE
author: windows-driver-content
description: The PEP_ACPI_GPIO_RESOURCE structure describes the ACPI configuration for a general purpose input/output (GPIO) resource.
old-location: kernel\pep_acpi_gpio_resource.htm
old-project: kernel
ms.assetid: 1B8AD1A9-9EB0-49A8-B791-0453C768A974
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_ACPI_GPIO_RESOURCE, PEP_ACPI_GPIO_RESOURCE, *PPEP_ACPI_GPIO_RESOURCE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_ACPI_GPIO_RESOURCE
req.alt-loc: pepfx.h
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
---

# PEP_ACPI_GPIO_RESOURCE structure



## -description
<p>The <b>PEP_ACPI_GPIO_RESOURCE</b> structure describes the ACPI configuration for a general purpose input/output (GPIO) resource.</p>


## -syntax

````
typedef struct _PEP_ACPI_GPIO_RESOURCE {
  PEP_ACPI_RESOURCE_TYPE      Type;
  PEP_ACPI_RESOURCE_FLAGS     Flags;
  KINTERRUPT_MODE             InterruptType;
  KINTERRUPT_POLARITY         InterruptPolarity;
  GPIO_PIN_CONFIG_TYPE        PinConfig;
  GPIO_PIN_IORESTRICTION_TYPE IoRestrictionType;
  USHORT                      DriveStrength;
  USHORT                      DebounceTimeout;
  PUSHORT                     PinTable;
  USHORT                      PinCount;
  UCHAR                       ResourceSourceIndex;
  PUNICODE_STRING             ResourceSourceName;
  PUCHAR                      VendorData;
  USHORT                      VendorDataLength;
} PEP_ACPI_GPIO_RESOURCE, *PPEP_ACPI_GPIO_RESOURCE;
````


## -struct-fields
<dl>

### -field Type

<dd>
<p>A <a href="..\pepfx\ne-pepfx--pep-acpi-resource-type.md">PEP_ACPI_RESOURCE_TYPE</a> enumeration value that identifies the resource type for this ACPI resource.</p>
</dd>

### -field Flags

<dd>
<p>A <a href="..\pepfx\ns-pepfx--pep-acpi-resource-flags.md">PEP_ACPI_RESOURCE_FLAGS</a> structure that describes the capabilities of this ACPI resource.</p>
</dd>

### -field InterruptType

<dd>
<p>A <a href="..\wdm\ne-wdm--kinterrupt-mode.md">KINTERRUPT_MODE</a> enumeration value that identifies the interrupt type.</p>
</dd>

### -field InterruptPolarity

<dd>
<p>A <a href="..\wdm\ne-wdm--kinterrupt-polarity.md">KINTERRUPT_POLARITY</a> enumeration value that identifies how a device signals an interrupt request on an interrupt line.</p>
</dd>

### -field PinConfig

<dd>
<p>A <a href="..\pepfx\ne-pepfx--gpio-pin-config-type.md">GPIO_PIN_CONFIG_TYPE</a> enumeration value that identifies the GPIO pin configuration type.</p>
</dd>

### -field IoRestrictionType

<dd>
<p>A <a href="..\pepfx\ne-pepfx--gpio-pin-iorestriction-type.md">GPIO_PIN_IORESTRICTION_TYPE</a> enumeration value that identifies the type of IO that the pin supports.</p>
</dd>

### -field DriveStrength

<dd>
<p>Specifies the output drive capability of the pin, in hundredths of milliamperes. </p>
</dd>

### -field DebounceTimeout

<dd>
<p>Specifies the hardware debounce wait time, in hundredths of milliseconds.</p>
</dd>

### -field PinTable

<dd>
<p>A list of pin numbers on the resource that are described by this descriptor. </p>
</dd>

### -field PinCount

<dd>
<p>The number of pins in <b>PinTable</b>.</p>
</dd>

### -field ResourceSourceIndex

<dd>
<p>This member is always zero.</p>
</dd>

### -field ResourceSourceName

<dd>
<p>This member is always set to "ResourceConsumer."</p>
</dd>

### -field VendorData

<dd>
<p>A pointer to a raw data buffer containing vendor-defined byte data to be decoded by the OS driver. </p>
</dd>

### -field VendorDataLength

<dd>
<p>The size of the <b>VendorData</b> buffer.</p>
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
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\pepfx\ne-pepfx--pep-acpi-resource-type.md">PEP_ACPI_RESOURCE_TYPE</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--kinterrupt-mode.md">KINTERRUPT_MODE</a>
</dt>
<dt>
<a href="..\wdm\ne-wdm--kinterrupt-polarity.md">KINTERRUPT_POLARITY</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-acpi-resource-flags.md">PEP_ACPI_RESOURCE_FLAGS</a>
</dt>
<dt>
<a href="..\pepfx\ne-pepfx--gpio-pin-config-type.md">GPIO_PIN_CONFIG_TYPE</a>
</dt>
<dt>
<a href="..\pepfx\ne-pepfx--gpio-pin-iorestriction-type.md">GPIO_PIN_IORESTRICTION_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_GPIO_RESOURCE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
