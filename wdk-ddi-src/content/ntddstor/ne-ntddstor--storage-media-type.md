---
UID: NE.ntddstor._STORAGE_MEDIA_TYPE
title: STORAGE_MEDIA_TYPE
author: windows-driver-content
description: The STORAGE_MEDIA_TYPE enumeration is used in conjunction with the IOCTL_STORAGE_GET_MEDIA_TYPES_EX request to query the class driver for the types of media that a device supports.
old-location: storage\storage_media_type.htm
old-project: storage
ms.assetid: 70214b6e-92d2-418a-ad8a-8701df02fdc3
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_MEDIA_TYPE
req.alt-loc: ntddstor.h
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

# STORAGE_MEDIA_TYPE enumeration



## -description
<p>The STORAGE_MEDIA_TYPE enumeration is used in conjunction with the <a href="..\ntddstor\ni-ntddstor-ioctl-storage-get-media-types-ex.md">IOCTL_STORAGE_GET_MEDIA_TYPES_EX</a> request to query the class driver for the types of media that a device supports.</p>


## -syntax

````
typedef enum _STORAGE_MEDIA_TYPE { 
  DDS_4mm             = 0x20,
  MiniQic             = 0x21,
  Travan              = 0x22,
  QIC                 = 0x23,
  MP_8mm              = 0x24,
  AME_8mm             = 0x25,
  AIT1_8mm            = 0x26,
  DLT                 = 0x27,
  NCTP                = 0x28,
  IBM_3480            = 0x29,
  IBM_3490E           = 0x2A,
  IBM_Magstar_3590    = 0x2B,
  IBM_Magstar_MP      = 0x2C,
  STK_DATA_D3         = 0x2D,
  SONY_DTF            = 0x2E,
  DV_6mm              = 0x2F,
  DMI                 = 0x30,
  SONY_D2             = 0x31,
  CLEANER_CARTRIDGE   = 0x32,
  CD_ROM              = 0x33,
  CD_R                = 0x34,
  CD_RW               = 0x35,
  DVD_ROM             = 0x36,
  DVD_R               = 0x37,
  DVD_RW              = 0x38,
  MO_3_RW             = 0x39,
  MO_5_WO             = 0x3A,
  MO_5_RW             = 0x3B,
  MO_5_LIMDOW         = 0x3C,
  PC_5_WO             = 0x3D,
  PC_5_RW             = 0x3E,
  PD_5_RW             = 0x3F,
  ABL_5_WO            = 0x40,
  PINNACLE_APEX_5_RW  = 0x41,
  SONY_12_WO          = 0x42,
  PHILIPS_12_WO       = 0x43,
  HITACHI_12_WO       = 0x44,
  CYGNET_12_WO        = 0x45,
  KODAK_14_WO         = 0x46,
  MO_NFR_525          = 0x47,
  NIKON_12_RW         = 0x48,
  IOMEGA_ZIP          = 0x49,
  IOMEGA_JAZ          = 0x4A,
  SYQUEST_EZ135       = 0x4B,
  SYQUEST_EZFLYER     = 0x4C,
  SYQUEST_SYJET       = 0x4D,
  AVATAR_F2           = 0x4E,
  MP2_8mm             = 0x4F,
  DST_S               = 0x50,
  DST_M               = 0x51,
  DST_L               = 0x52,
  VXATape_1           = 0x53,
  VXATape_2           = 0x54,
  STK_9840            = 0x55,
  LTO_Ultrium         = 0x56,
  LTO_Accelis         = 0x57,
  DVD_RAM             = 0x58,
  AIT_8mm             = 0x59,
  ADR_1               = 0x5A,
  ADR_2               = 0x5B,
  STK_9940            = 0x5C,
  SAIT                = 0x5D,
  VXATape             = 0x5E
} STORAGE_MEDIA_TYPE, *PSTORAGE_MEDIA_TYPE;
````


## -enum-fields
<dl>

### -field DDS_4mm

<dd>
<p>Indicates a DAT DDS1 or DDS2 tape device (all vendors).</p>
</dd>

### -field MiniQic

<dd>
<p>Indicates a mini-QIC tape device. </p>
</dd>

### -field Travan

<dd>
<p>Indicates a Travan TR-1, 2 or 3 tape device. </p>
</dd>

### -field QIC

<dd>
<p>Indicates a QIC tape device. </p>
</dd>

### -field MP_8mm

<dd>
<p>Indicates an 8mm Exabyte metal particle tape device. </p>
</dd>

### -field AME_8mm

<dd>
<p>Indicates an 8mm Exabyte advanced metal tape device.</p>
</dd>

### -field AIT1_8mm

<dd>
<p>Indicates an 8mm Sony AIT tape device. </p>
</dd>

### -field DLT

<dd>
<p>Indicates a DLT compact IIIxt or IV tape device. </p>
</dd>

### -field NCTP

<dd>
<p>Indicates a Philips NCTP tape device. </p>
</dd>

### -field IBM_3480

<dd>
<p>Indicates an IBM 3480 tape device. </p>
</dd>

### -field IBM_3490E

<dd>
<p>Indicates an IBM 3490E tape device.</p>
</dd>

### -field IBM_Magstar_3590

<dd>
<p>Indicates an IBM Magstar 3590 tape device. </p>
</dd>

### -field IBM_Magstar_MP

<dd>
<p>Indicates an IBM Magstar MP tape device. </p>
</dd>

### -field STK_DATA_D3

<dd>
<p>Indicates an STK data D3 tape device. </p>
</dd>

### -field SONY_DTF

<dd>
<p>Indicates a Sony DTF tape device. </p>
</dd>

### -field DV_6mm

<dd>
<p>Indicates a 6mm digital video tape device. </p>
</dd>

### -field DMI

<dd>
<p>Indicates a Exabyte DMI tape device and compatible devices. </p>
</dd>

### -field SONY_D2

<dd>
<p>Indicates a Sony D2S or D2L tape device. </p>
</dd>

### -field CLEANER_CARTRIDGE

<dd>
<p>Indicates a drive type that supports drive cleaners. </p>
</dd>

### -field CD_ROM

<dd>
<p>Indicates a CD optical disk. </p>
</dd>

### -field CD_R

<dd>
<p>Indicates a CD-recordable (write once) optical disk. </p>
</dd>

### -field CD_RW

<dd>
<p>Indicates a CD-rewritable optical disk. </p>
</dd>

### -field DVD_ROM

<dd>
<p>Indicates a DVD-ROM optical disk. </p>
</dd>

### -field DVD_R

<dd>
<p>Indicates a DVD-recordable (write once) optical disk. </p>
</dd>

### -field DVD_RW

<dd>
<p>Indicates a DVD-rewritable optical disk. </p>
</dd>

### -field MO_3_RW

<dd>
<p>Indicates a 3.5" rewritable MO optical disk. </p>
</dd>

### -field MO_5_WO

<dd>
<p>Indicates a MO 5.25" write once optical disk. </p>
</dd>

### -field MO_5_RW

<dd>
<p>Indicates a MO 5.25" rewritable (not LIMDOW) optical disk.</p>
</dd>

### -field MO_5_LIMDOW

<dd>
<p>Indicates a MO 5.25" rewritable (LIMDOW) optical disk. </p>
</dd>

### -field PC_5_WO

<dd>
<p>Indicates a phase change 5.25" write once optical disk. </p>
</dd>

### -field PC_5_RW

<dd>
<p>Indicates a phase change 5.25" rewritable optical disk. </p>
</dd>

### -field PD_5_RW

<dd>
<p>Indicates a phase change dual rewritable optical disk. </p>
</dd>

### -field ABL_5_WO

<dd>
<p>Indicates a ablative 5.25" write once optical disk. </p>
</dd>

### -field PINNACLE_APEX_5_RW

<dd>
<p>Indicates a pinnacle apex 4.6-GB rewritable optical disk.</p>
</dd>

### -field SONY_12_WO

<dd>
<p>Indicates a Sony 12" write once optical disk. </p>
</dd>

### -field PHILIPS_12_WO

<dd>
<p>Indicates a Philips/LMS 12" write once optical disk. </p>
</dd>

### -field HITACHI_12_WO

<dd>
<p>Indicates a Hitachi 12" write once optical disk. </p>
</dd>

### -field CYGNET_12_WO

<dd>
<p>Indicates a Cygnet/ATG 12" write once optical disk. </p>
</dd>

### -field KODAK_14_WO

<dd>
<p>Indicates a Kodak 14" write once optical disk. </p>
</dd>

### -field MO_NFR_525

<dd>
<p>Indicates a near field recording (Terastor) optical disk. </p>
</dd>

### -field NIKON_12_RW

<dd>
<p>Indicates a Nikon 12" rewritable optical disk. </p>
</dd>

### -field IOMEGA_ZIP

<dd>
<p>Indicates Iomega zip magnetic disk device. </p>
</dd>

### -field IOMEGA_JAZ

<dd>
<p>Indicates an Iomega Jaz magnetic disk device. </p>
</dd>

### -field SYQUEST_EZ135

<dd>
<p>Indicates a Syquest EZ135 magnetic disk device. </p>
</dd>

### -field SYQUEST_EZFLYER

<dd>
<p>Indicates a Syquest EzFlyer magnetic disk device. </p>
</dd>

### -field SYQUEST_SYJET

<dd>
<p>Indicates a Syquest SyJet magnetic disk device. </p>
</dd>

### -field AVATAR_F2

<dd>
<p>Indicates a 2.5" Floppy device. </p>
</dd>

### -field MP2_8mm

<dd>
<p>Indicates an 8mm Hitachi tape device. </p>
</dd>

### -field DST_S

<dd>
<p>Indicates a type DST Ampex small tape device. </p>
</dd>

### -field DST_M

<dd>
<p>Indicates a type DST Ampex medium tape device. </p>
</dd>

### -field DST_L

<dd>
<p>Indicates a type DST Ampex large tape device. </p>
</dd>

### -field VXATape_1

<dd>
<p>Indicates an 8mm Ecrix tape device. </p>
</dd>

### -field VXATape_2

<dd>
<p>Indicates an 8mm Ecrix tape device. </p>
</dd>

### -field STK_9840

<dd>
<p>Indicates an STK 9840 device. </p>
</dd>

### -field LTO_Ultrium

<dd>
<p>Indicates an IBM, HP, or Seagate LTO Ultrium device. </p>
</dd>

### -field LTO_Accelis

<dd>
<p>Indicates an IBM, HP, or Seagate LTO Accelis</p>
</dd>

### -field DVD_RAM

<dd>
<p>Indicates a DVD-RAM optical device. </p>
</dd>

### -field AIT_8mm

<dd>
<p>Indicates an AIT2 or higher 8mm tape device. </p>
</dd>

### -field ADR_1

<dd>
<p>Indicates an on-stream ADR media type device. </p>
</dd>

### -field ADR_2

<dd>
<p>Indicates an on-stream ADR media type device. </p>
</dd>

### -field STK_9940

<dd>
<p>STK 9940</p>
</dd>

### -field SAIT

<dd>
<p>SAIT Tapes</p>
</dd>

### -field VXATape

<dd>
<p>VXA (Ecrix 8mm) Tape</p>
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
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddstor\ns-ntddstor--device-media-info.md">DEVICE_MEDIA_INFO</a>
</dt>
<dt>
<a href="..\ntddstor\ns-ntddstor--get-media-types.md">GET_MEDIA_TYPES</a>
</dt>
<dt>
<a href="..\ntddstor\ni-ntddstor-ioctl-storage-get-media-types-ex.md">IOCTL_STORAGE_GET_MEDIA_TYPES_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_MEDIA_TYPE enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
