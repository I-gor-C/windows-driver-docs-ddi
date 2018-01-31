---
UID : NE:ntddstor._STORAGE_MEDIA_TYPE
title : "_STORAGE_MEDIA_TYPE"
author : windows-driver-content
description : The STORAGE_MEDIA_TYPE enumeration is used in conjunction with the IOCTL_STORAGE_GET_MEDIA_TYPES_EX request to query the class driver for the types of media that a device supports.
old-location : storage\storage_media_type.htm
old-project : storage
ms.assetid : 70214b6e-92d2-418a-ad8a-8701df02fdc3
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IOMEGA_JAZ, ntddstor/DVD_RW, ntddstor/DVD_R, IBM_3480, ntddstor/SONY_12_WO, CD_RW, ntddstor/VXATape_2, ntddstor/ABL_5_WO, storage.storage_media_type, ntddstor/AIT_8mm, ABL_5_WO, ntddstor/DVD_RAM, MO_3_RW, ntddstor/IBM_Magstar_3590, ntddstor/MP2_8mm, IOMEGA_ZIP, ntddstor/PSTORAGE_MEDIA_TYPE, PSTORAGE_MEDIA_TYPE, ntddstor/PC_5_WO, HITACHI_12_WO, ntddstor/ADR_1, DST_S, ntddstor/DV_6mm, ntddstor/SONY_DTF, ntddstor/SYQUEST_EZ135, MP_8mm, ntddstor/IBM_3490E, ntddstor/AME_8mm, SYQUEST_SYJET, STORAGE_MEDIA_TYPE, ntddstor/MO_5_LIMDOW, ntddstor/MO_NFR_525, AIT_8mm, ntddstor/ADR_2, PD_5_RW, ntddstor/DDS_4mm, DST_M, PSTORAGE_MEDIA_TYPE enumeration pointer [Storage Devices], ntddstor/PC_5_RW, ntddstor/PD_5_RW, ntddstor/SAIT, IBM_Magstar_3590, ntddstor/PINNACLE_APEX_5_RW, STK_9940, ntddstor/STK_9940, CD_ROM, ntddstor/DMI, ntddstor/MiniQic, MO_5_RW, ntddstor/HITACHI_12_WO, STK_DATA_D3, MiniQic, ntddstor/NIKON_12_RW, DDS_4mm, LTO_Accelis, ntddstor/MP_8mm, ntddstor/NCTP, MO_5_WO, VXATape, IBM_Magstar_MP, ntddstor/QIC, LTO_Ultrium, ntddstor/VXATape_1, ntddstor/CLEANER_CARTRIDGE, Travan, ntddstor/IOMEGA_ZIP, ntddstor/SONY_D2, DVD_RW, ADR_1, structs-general_d1e0e1bc-5ce9-49d0-9ab5-94b5e495d124.xml, ntddstor/CYGNET_12_WO, PC_5_WO, ntddstor/MO_3_RW, SYQUEST_EZ135, ntddstor/STK_9840, _STORAGE_MEDIA_TYPE, KODAK_14_WO, IBM_3490E, ntddstor/CD_R, ntddstor/AVATAR_F2, DST_L, STORAGE_MEDIA_TYPE enumeration [Storage Devices], SONY_DTF, ntddstor/DST_L, PC_5_RW, SYQUEST_EZFLYER, ntddstor/SYQUEST_SYJET, SAIT, VXATape_2, DVD_R, ntddstor/DLT, ntddstor/LTO_Accelis, ntddstor/AIT1_8mm, *PSTORAGE_MEDIA_TYPE, CLEANER_CARTRIDGE, ntddstor/MO_5_WO, ntddstor/IBM_Magstar_MP, SONY_D2, ntddstor/SYQUEST_EZFLYER, ntddstor/KODAK_14_WO, PINNACLE_APEX_5_RW, AIT1_8mm, DVD_RAM, AME_8mm, NIKON_12_RW, NCTP, ntddstor/LTO_Ultrium, ntddstor/MO_5_RW, SONY_12_WO, DMI, ntddstor/STK_DATA_D3, ntddstor/IBM_3480, AVATAR_F2, ntddstor/PHILIPS_12_WO, ntddstor/VXATape, ntddstor/Travan, ADR_2, STK_9840, ntddstor/DST_S, MO_5_LIMDOW, DV_6mm, MP2_8mm, ntddstor/CD_ROM, DVD_ROM, PHILIPS_12_WO, ntddstor/DVD_ROM, QIC, CD_R, ntddstor/STORAGE_MEDIA_TYPE, ntddstor/CD_RW, ntddstor/DST_M, CYGNET_12_WO, DLT, ntddstor/IOMEGA_JAZ, VXATape_1, MO_NFR_525
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddstor.h
req.include-header : Ntddstor.h
req.target-type : Windows
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
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : STORAGE_MEDIA_TYPE, *PSTORAGE_MEDIA_TYPE
---

# _STORAGE_MEDIA_TYPE Enumeration
The STORAGE_MEDIA_TYPE enumeration is used in conjunction with the <a href="..\ntddstor\ni-ntddstor-ioctl_storage_get_media_types_ex.md">IOCTL_STORAGE_GET_MEDIA_TYPES_EX</a> request to query the class driver for the types of media that a device supports.

## Syntax
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

## Constants

<table>

<tr>
<td>ABL_5_WO</td>
<td>Indicates a ablative 5.25" write once optical disk.</td>
</tr>

<tr>
<td>ADR_1</td>
<td>Indicates an on-stream ADR media type device.</td>
</tr>

<tr>
<td>ADR_2</td>
<td>Indicates an on-stream ADR media type device.</td>
</tr>

<tr>
<td>AIT_8mm</td>
<td>Indicates an AIT2 or higher 8mm tape device.</td>
</tr>

<tr>
<td>AIT1_8mm</td>
<td>Indicates an 8mm Sony AIT tape device.</td>
</tr>

<tr>
<td>AME_8mm</td>
<td>Indicates an 8mm Exabyte advanced metal tape device.</td>
</tr>

<tr>
<td>AVATAR_F2</td>
<td>Indicates a 2.5" Floppy device.</td>
</tr>

<tr>
<td>CD_R</td>
<td>Indicates a CD-recordable (write once) optical disk.</td>
</tr>

<tr>
<td>CD_ROM</td>
<td>Indicates a CD optical disk.</td>
</tr>

<tr>
<td>CD_RW</td>
<td>Indicates a CD-rewritable optical disk.</td>
</tr>

<tr>
<td>CLEANER_CARTRIDGE</td>
<td>Indicates a drive type that supports drive cleaners.</td>
</tr>

<tr>
<td>CYGNET_12_WO</td>
<td>Indicates a Cygnet/ATG 12" write once optical disk.</td>
</tr>

<tr>
<td>DDS_4mm</td>
<td>Indicates a DAT DDS1 or DDS2 tape device (all vendors).</td>
</tr>

<tr>
<td>DLT</td>
<td>Indicates a DLT compact IIIxt or IV tape device.</td>
</tr>

<tr>
<td>DMI</td>
<td>Indicates a Exabyte DMI tape device and compatible devices.</td>
</tr>

<tr>
<td>DST_L</td>
<td>Indicates a type DST Ampex large tape device.</td>
</tr>

<tr>
<td>DST_M</td>
<td>Indicates a type DST Ampex medium tape device.</td>
</tr>

<tr>
<td>DST_S</td>
<td>Indicates a type DST Ampex small tape device.</td>
</tr>

<tr>
<td>DV_6mm</td>
<td>Indicates a 6mm digital video tape device.</td>
</tr>

<tr>
<td>DVD_R</td>
<td>Indicates a DVD-recordable (write once) optical disk.</td>
</tr>

<tr>
<td>DVD_RAM</td>
<td>Indicates a DVD-RAM optical device.</td>
</tr>

<tr>
<td>DVD_ROM</td>
<td>Indicates a DVD-ROM optical disk.</td>
</tr>

<tr>
<td>DVD_RW</td>
<td>Indicates a DVD-rewritable optical disk.</td>
</tr>

<tr>
<td>HITACHI_12_WO</td>
<td>Indicates a Hitachi 12" write once optical disk.</td>
</tr>

<tr>
<td>IBM_3480</td>
<td>Indicates an IBM 3480 tape device.</td>
</tr>

<tr>
<td>IBM_3490E</td>
<td>Indicates an IBM 3490E tape device.</td>
</tr>

<tr>
<td>IBM_Magstar_3590</td>
<td>Indicates an IBM Magstar 3590 tape device.</td>
</tr>

<tr>
<td>IBM_Magstar_MP</td>
<td>Indicates an IBM Magstar MP tape device.</td>
</tr>

<tr>
<td>IOMEGA_JAZ</td>
<td>Indicates an Iomega Jaz magnetic disk device.</td>
</tr>

<tr>
<td>IOMEGA_ZIP</td>
<td>Indicates Iomega zip magnetic disk device.</td>
</tr>

<tr>
<td>KODAK_14_WO</td>
<td>Indicates a Kodak 14" write once optical disk.</td>
</tr>

<tr>
<td>LTO_Accelis</td>
<td>Indicates an IBM, HP, or Seagate LTO Accelis</td>
</tr>

<tr>
<td>LTO_Ultrium</td>
<td>Indicates an IBM, HP, or Seagate LTO Ultrium device.</td>
</tr>

<tr>
<td>MiniQic</td>
<td>Indicates a mini-QIC tape device.</td>
</tr>

<tr>
<td>MO_3_RW</td>
<td>Indicates a 3.5" rewritable MO optical disk.</td>
</tr>

<tr>
<td>MO_5_LIMDOW</td>
<td>Indicates a MO 5.25" rewritable (LIMDOW) optical disk.</td>
</tr>

<tr>
<td>MO_5_RW</td>
<td>Indicates a MO 5.25" rewritable (not LIMDOW) optical disk.</td>
</tr>

<tr>
<td>MO_5_WO</td>
<td>Indicates a MO 5.25" write once optical disk.</td>
</tr>

<tr>
<td>MO_NFR_525</td>
<td>Indicates a near field recording (Terastor) optical disk.</td>
</tr>

<tr>
<td>MP_8mm</td>
<td>Indicates an 8mm Exabyte metal particle tape device.</td>
</tr>

<tr>
<td>MP2_8mm</td>
<td>Indicates an 8mm Hitachi tape device.</td>
</tr>

<tr>
<td>NCTP</td>
<td>Indicates a Philips NCTP tape device.</td>
</tr>

<tr>
<td>NIKON_12_RW</td>
<td>Indicates a Nikon 12" rewritable optical disk.</td>
</tr>

<tr>
<td>PC_5_RW</td>
<td>Indicates a phase change 5.25" rewritable optical disk.</td>
</tr>

<tr>
<td>PC_5_WO</td>
<td>Indicates a phase change 5.25" write once optical disk.</td>
</tr>

<tr>
<td>PD_5_RW</td>
<td>Indicates a phase change dual rewritable optical disk.</td>
</tr>

<tr>
<td>PHILIPS_12_WO</td>
<td>Indicates a Philips/LMS 12" write once optical disk.</td>
</tr>

<tr>
<td>PINNACLE_APEX_5_RW</td>
<td>Indicates a pinnacle apex 4.6-GB rewritable optical disk.</td>
</tr>

<tr>
<td>QIC</td>
<td>Indicates a QIC tape device.</td>
</tr>

<tr>
<td>SAIT</td>
<td>SAIT Tapes</td>
</tr>

<tr>
<td>SONY_12_WO</td>
<td>Indicates a Sony 12" write once optical disk.</td>
</tr>

<tr>
<td>SONY_D2</td>
<td>Indicates a Sony D2S or D2L tape device.</td>
</tr>

<tr>
<td>SONY_DTF</td>
<td>Indicates a Sony DTF tape device.</td>
</tr>

<tr>
<td>STK_9940</td>
<td>STK 9940</td>
</tr>

<tr>
<td>STK_DATA_D3</td>
<td>Indicates an STK data D3 tape device.</td>
</tr>

<tr>
<td>STK_EAGLE</td>
<td></td>
</tr>

<tr>
<td>SYQUEST_EZ135</td>
<td>Indicates a Syquest EZ135 magnetic disk device.</td>
</tr>

<tr>
<td>SYQUEST_EZFLYER</td>
<td>Indicates a Syquest EzFlyer magnetic disk device.</td>
</tr>

<tr>
<td>SYQUEST_SYJET</td>
<td>Indicates a Syquest SyJet magnetic disk device.</td>
</tr>

<tr>
<td>Travan</td>
<td>Indicates a Travan TR-1, 2 or 3 tape device.</td>
</tr>

<tr>
<td>VXATape</td>
<td>VXA (Ecrix 8mm) Tape</td>
</tr>

<tr>
<td>VXATape_1</td>
<td>Indicates an 8mm Ecrix tape device.</td>
</tr>

<tr>
<td>VXATape_2</td>
<td>Indicates an 8mm Ecrix tape device.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddstor.h (include Ntddstor.h) |

## See Also

<a href="..\ntddstor\ns-ntddstor-_get_media_types.md">GET_MEDIA_TYPES</a>

<a href="..\ntddstor\ns-ntddstor-_device_media_info.md">DEVICE_MEDIA_INFO</a>

<a href="..\ntddstor\ni-ntddstor-ioctl_storage_get_media_types_ex.md">IOCTL_STORAGE_GET_MEDIA_TYPES_EX</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_MEDIA_TYPE enumeration%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>