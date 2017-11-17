---
UID: NS.windowssideshowclassextension.ISideShowDriverVtbl
title: ISideShowDriverVtbl
author: windows-driver-content
description: 
ms.assetid: 20eca303-889f-442b-a8e5-5d4894a16ad5
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: ISideShowDriverVtbl, ISideShowDriverVtbl
req.header: windowssideshowclassextension.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# ISideShowDriverVtbl structure

## -description



## -struct-fields

### -field HRESULT(* )(ISideShowDriver *This,REFIID riid, void **ppvObject) QueryInterface			
 	
### -field ULONG(* )(ISideShowDriver *This) AddRef			
 	
### -field ULONG(* )(ISideShowDriver *This) Release			
 	
### -field HRESULT(* )(ISideShowDriver *This,LPWSTR *ppwszName) OnGetDeviceName			
 	
### -field HRESULT(* )(ISideShowDriver *This,LPWSTR *ppwszManufacturer) OnGetDeviceManufacturer			
 	
### -field HRESULT(* )(ISideShowDriver *This,LPWSTR *ppwszVersion) OnGetDeviceFirmwareVersion			
 	
### -field HRESULT(* )(ISideShowDriver *This, const FILETIME FileTime) OnSetTime			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SIDESHOW_TIME_ZONE_INFORMATION *pTimeZoneInformation) OnSetTimeZone			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid) OnSetCurrentUser			
 	
### -field HRESULT(* )(ISideShowDriver *This,SID **ppUserSid) OnGetCurrentUser			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid, const USER_STATE state) OnSetUserState			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,LPCWSTR pwszDateFormat) OnSetShortDateFormat			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,LPCWSTR pwszDateFormat) OnSetLongDateFormat			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,LPCWSTR pwszTimeFormat) OnSetShortTimeFormat			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,LPCWSTR pwszTimeFormat) OnSetLongTimeFormat			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,LPCWSTR pwszLanguage) OnSetLanguage			
 	
### -field HRESULT(* )(ISideShowDriver *This,ENDPOINT_ID **rgEndpoints,DWORD *pcEndpoints) OnGetDeviceEndpoints			
 	
### -field HRESULT(* )(ISideShowDriver *This, const PROPERTYKEY *pKey,PROPVARIANT *pvValue) OnGetDeviceCapabilities			
 	
### -field HRESULT(* )(ISideShowDriver *This,APPLICATION_ID **ppApplicationIds,ENDPOINT_ID **ppEndpointIds,DWORD *pcApplications) OnGetPreEnabledApplications			
 	
### -field HRESULT(* )(ISideShowDriver *This, const APPLICATION_ID *pApplicationIds, const DWORD cApplicationIds) OnSetApplicationOrder			
 	
### -field HRESULT(* )(ISideShowDriver *This,APPLICATION_ID **ppApplicationIds,DWORD *pcApplicationIds) OnGetApplicationOrder			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,REFAPPLICATION_ID ApplicationId,REFENDPOINT_ID EndPointId,LPCWSTR pcwszName, const DWORD dwCachePolicy, const DWORD dwOnlineOnly, const unsigned char *pbLargeIcon, const DWORD cbLargeIcon, const unsigned char *pbMediumIcon, const DWORD cbMediumIcon, const unsigned char *pbSmallIcon, const DWORD cbSmallIcon) OnAddApplication			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,REFAPPLICATION_ID ApplicationId) OnRemoveApplication			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid) OnRemoveAllApplications			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,REFAPPLICATION_ID ApplicationId,REFENDPOINT_ID EndpointId, const CONTENT_ID ContentId, const unsigned char *pData, const DWORD cbData) OnAddContent			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,REFAPPLICATION_ID ApplicationId,REFENDPOINT_ID EndpointId, const CONTENT_ID ContentId) OnRemoveContent			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,REFAPPLICATION_ID ApplicationId,REFENDPOINT_ID EndpointId) OnRemoveAllContent			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,REFAPPLICATION_ID ApplicationId, const NOTIFICATION_ID NotificationId, const FILETIME ftExpiration,LPCWSTR pcwszTitle,LPCWSTR pcwszMessage, const unsigned char *pbImage, const DWORD cbImage) OnAddNotification			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,REFAPPLICATION_ID ApplicationId, const NOTIFICATION_ID NotificationId) OnRemoveNotification			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid,REFAPPLICATION_ID ApplicationId) OnRemoveAllNotifications			
 	
### -field HRESULT(* )(ISideShowDriver *This, const SID *pUserSid, const BOOL fIsEnabled) OnSetNotificationsEnabled			
 	
### -field HRESULT(* )(ISideShowDriver *This,IUnknown *pPortableDeviceValuesParams,IUnknown *pPortableDeviceValuesResults) OnProcessWpdMessage			
 	
## -remarks

## -see-also